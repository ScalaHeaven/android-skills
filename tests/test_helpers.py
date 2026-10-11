"""Exercise the seven helper CLIs with valid and invalid local fixtures."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


class HelperTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "fixtures with spaces"
        self.root.mkdir()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def run_helper(self, skill, script, *args, code=0):
        result = subprocess.run(
            [sys.executable, "-B", str(ROOT / skill / "scripts" / script),
             *(str(arg) for arg in args)],
            capture_output=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            timeout=15,
        )
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        if code == 2 and not result.stdout:
            self.assertIn("error:", result.stderr)
            return {}
        return json.loads(result.stdout)

    def manifest(self, path, code=0):
        return self.run_helper("audit-android-components", "inspect_manifest.py", path, code=code)

    def test_manifest_preserves_declared_permissions_without_inferred_defaults(self):
        path = self.write("AndroidManifest.xml", '''<manifest
            xmlns:android="http://schemas.android.com/apk/res/android" package="example.app">
          <uses-permission android:name="android.permission.CAMERA"/>
          <application android:permission="example.PRIVATE">
            <activity android:name=".Main"><intent-filter>
              <action android:name="android.intent.action.VIEW"/>
            </intent-filter></activity>
            <service android:name=".Sync" android:exported="false"/>
          </application>
        </manifest>''')
        result = self.manifest(path)
        self.assertEqual(result["permissions"], ["android.permission.CAMERA"])
        main, service = result["components"]
        self.assertIsNone(main["exported_declared"])
        self.assertEqual(main["permission"], "example.PRIVATE")
        self.assertEqual(main["actions"], ["android.intent.action.VIEW"])
        self.assertEqual(service["exported_declared"], "false")

    def test_manifest_rejects_malformed_xml_and_wrong_root(self):
        for source in ("<manifest>", "<other/>"):
            with self.subTest(source=source):
                self.manifest(self.write("bad.xml", source), code=2)

    def test_apk_inventory_reports_abis_sizes_and_does_not_extract(self):
        path = self.root / "sample.apk"
        with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
            archive.writestr("lib/arm64-v8a/libsample.so", b"1234")
            archive.writestr("base/lib/x86_64/libsample.so", b"123")
            archive.writestr("../outside.txt", b"never extract")
        result = self.run_helper("audit-android-release-build", "inspect_apk.py", path)
        self.assertEqual(result["abis"], ["arm64-v8a", "x86_64"])
        self.assertEqual(result["entries"], 3)
        self.assertEqual(result["native_libraries"][0]["bytes"], 4)
        self.assertFalse((self.root.parent / "outside.txt").exists())

    def test_apk_rejects_invalid_zip(self):
        self.run_helper("audit-android-release-build", "inspect_apk.py",
                        self.write("bad.apk", "not a zip"), code=2)

    def benchmark(self, before, after, code=0):
        return self.run_helper(
            "benchmark-android-application", "compare_samples.py",
            self.write("before.json", json.dumps(before)),
            self.write("after.json", json.dumps(after)), code=code,
        )

    def test_benchmark_medians_and_context_mismatch(self):
        result = self.benchmark(
            {"metric": "startup", "unit": "ms", "samples": [10, 20, 30], "context": "A"},
            {"metric": "startup", "unit": "ms", "samples": [20, 40, 60], "context": "B"},
        )
        self.assertEqual(result["median_change_percent"], 100)
        self.assertEqual(result["before"]["median"], 20)
        self.assertFalse(result["contexts_match"])
        self.assertTrue(result["context_recorded"])

    def test_benchmark_zero_baseline_has_no_percentage(self):
        sample = {"metric": "time", "unit": "ms", "samples": [0]}
        self.assertIsNone(self.benchmark(sample, sample)["median_change_percent"])

    def test_benchmark_rejects_invalid_samples_and_mismatched_units(self):
        valid = {"metric": "time", "unit": "ms", "samples": [1]}
        for values in ([], [True], [-1], [float("nan")], [float("inf")]):
            with self.subTest(values=values):
                self.benchmark({**valid, "samples": values}, valid, code=2)
        self.benchmark(valid, {**valid, "unit": "s"}, code=2)

    def report(self, source, code=0):
        return self.run_helper("debug-android-flaky-tests", "summarize_test_reports.py",
                               self.write("report.xml", source), code=code)

    def test_junit_counts_outcomes_and_omits_failure_messages(self):
        result = self.report('''<testsuite tests="999">
          <testcase name="pass" time="0.1"/>
          <testcase name="fail" time="2"><failure>secret-token</failure></testcase>
          <testcase name="error"><error>secret-token</error></testcase>
          <testcase name="skip"><skipped/></testcase>
        </testsuite>''', code=1)
        self.assertEqual(result["counts"], {"passed": 1, "failed": 1, "errored": 1, "skipped": 1})
        self.assertEqual(result["test_cases"], 4)
        self.assertEqual(result["slowest"][0]["name"], "fail")
        self.assertNotIn("secret-token", json.dumps(result))

    def test_junit_rejects_bad_reports_without_retaining_partial_counts(self):
        for source in ("<broken", "<other/>", '<testsuite><testcase/><testcase time="nan"/></testsuite>'):
            with self.subTest(source=source):
                result = self.report(source, code=2)
                self.assertEqual(result["test_cases"], 0)
                self.assertEqual(len(result["invalid_reports"]), 1)

    def test_junit_empty_report_and_success_exit_codes(self):
        self.assertEqual(self.report("<testsuite/>", code=2)["test_cases"], 0)
        self.assertEqual(self.report("<testsuite><testcase/></testsuite>")["counts"]["passed"], 1)

    def test_project_inventory_ignores_build_outputs_comments_and_secrets(self):
        self.write("app/build.gradle.kts", '// minSdk = 1\nandroid { minSdk = 24; targetSdk = 35 }\npassword = "secret-token"')
        self.write("build/build.gradle", "compileSdk = 999")
        self.write("gradle/wrapper/gradle-wrapper.properties", "secret-token")
        result = self.run_helper("develop-android-gradle-build", "project_inventory.py", self.root)
        self.assertEqual([entry["path"] for entry in result["files"]],
                         ["app/build.gradle.kts", "gradle/wrapper/gradle-wrapper.properties"])
        self.assertEqual([hint["literal_value"] for hint in result["files"][0]["sdk_hints"]], [24, 35])
        self.assertNotIn("secret-token", json.dumps(result))

    def test_project_inventory_rejects_missing_directory(self):
        self.run_helper("develop-android-gradle-build", "project_inventory.py", self.root / "missing", code=2)

    def schemas(self, before, after, code=0):
        return self.run_helper("develop-android-room", "compare_schemas.py",
                               self.write("old.json", json.dumps({"database": before})),
                               self.write("new.json", json.dumps({"database": after})), code=code)

    def test_room_schema_inventory_reports_structural_changes(self):
        result = self.schemas(
            {"version": 1, "entities": [{"tableName": "trip", "fields": []}, {"tableName": "old"}]},
            {"version": 2, "entities": [{"tableName": "trip", "fields": ["distance"]}, {"tableName": "new"}], "views": ["summary"]},
        )
        self.assertEqual(result["added_tables"], ["new"])
        self.assertEqual(result["removed_tables"], ["old"])
        self.assertEqual(result["changed_tables"], [{"table": "trip", "changed_sections": ["fields"]}])
        self.assertTrue(result["views_changed"])

    def test_room_schema_rejects_duplicate_tables(self):
        self.schemas({"entities": [{"tableName": "trip"}, {"tableName": "trip"}]},
                     {"entities": []}, code=2)

    def graph(self, data, code=0):
        return self.run_helper("modularize-android-project", "analyze_graph.py",
                               self.write("graph.json", json.dumps(data)), code=code)

    def test_graph_orders_dependencies_before_dependents(self):
        order = self.graph({"app": ["data"], "data": ["core"], "core": []})["dependency_first_order"]
        self.assertEqual(order, ["core", "data", "app"])

    def test_graph_reports_cycles_and_undeclared_nodes(self):
        cycle = self.graph({"a": ["b"], "b": ["a"]}, code=1)
        self.assertEqual(cycle["cycles"], [["a", "b", "a"]])
        self.assertIsNone(cycle["dependency_first_order"])
        self.assertEqual(self.graph({"app": ["missing"]}, code=1)["undeclared_nodes"], ["missing"])

    def test_graph_rejects_invalid_adjacency_data(self):
        self.graph({"app": "data"}, code=2)


if __name__ == "__main__":
    unittest.main()
