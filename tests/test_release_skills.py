"""Validate release contents and reject broken metadata and local links."""

import subprocess
import tempfile
import unittest
from pathlib import Path
from urllib.parse import quote
from zipfile import ZipFile

from scripts.release_skills import package


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "repo with spaces & data"
        self.root.mkdir()
        self.write("README.md", "# Test skills\n")
        self.write("sample-skill/SKILL.md",
                   '---\nname: sample-skill\ndescription: "A sample skill."\n---\n\n'
                   '# Sample\n\nRead [the reference](references/example.md).\n')
        self.write("sample-skill/agents/openai.yaml",
                   'interface:\n  display_name: "Sample Skill"\n'
                   '  short_description: "A skill for validating release archives"\n'
                   '  default_prompt: "Use $sample-skill for this task."\n')
        self.write("sample-skill/references/example.md", "Sample reference.\n")
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.track()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def track(self):
        subprocess.run(["git", "add", "--all"], cwd=self.root, check=True)

    def package(self):
        output = self.root / "dist" / "skills.zip"
        package(self.root, output)
        return output

    def test_archive_keeps_resources_and_excludes_repository_artifacts(self):
        for name in ("tests/test_example.py", "scripts/tool.py", ".github/workflows/ci.yml",
                     "sample-skill/.DS_Store", "sample-skill/__pycache__/example.pyc",
                     "sample-skill/venv/example.py", "sample-skill/build/output.txt"):
            self.write(name, "not a skill resource\n")
        self.write("sample-skill/scripts/helper.py", "print('sample')\n")
        self.track()
        self.write("sample-skill/references/untracked.md", "not tracked\n")
        with ZipFile(self.package()) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), {
                "README.md", "sample-skill/SKILL.md", "sample-skill/agents/openai.yaml",
                "sample-skill/references/example.md", "sample-skill/scripts/helper.py",
            })

    def test_crlf_encoded_paths_and_zip_round_trip(self):
        name = "references/caf\u00e9 notes.md"
        path = self.write(f"sample-skill/{name}", "UTF-8 reference: \u2200\n")
        skill = self.root / "sample-skill/SKILL.md"
        source = skill.read_text(encoding="utf-8") + f"\nRead [data]({quote(name)}).\n"
        skill.write_bytes(source.replace("\n", "\r\n").encode("utf-8"))
        self.track()
        with ZipFile(self.package()) as archive:
            self.assertIsNone(archive.testzip())
            self.assertTrue(all("\\" not in entry for entry in archive.namelist()))
            self.assertEqual(archive.read(f"sample-skill/{name}"), path.read_bytes())
            self.assertEqual(archive.read("sample-skill/SKILL.md"), skill.read_bytes())

    def test_rejects_name_mismatch(self):
        path = self.root / "sample-skill/SKILL.md"
        path.write_text(path.read_text().replace("name: sample-skill", "name: other"))
        with self.assertRaisesRegex(ValueError, "name must match"):
            self.package()

    def test_rejects_missing_frontmatter(self):
        self.write("sample-skill/SKILL.md", "# Instructions\n")
        with self.assertRaisesRegex(ValueError, "frontmatter"):
            self.package()

    def test_rejects_empty_description_and_instructions(self):
        for source, message in (
            ('---\nname: sample-skill\ndescription: ""\n---\n# Sample\n', "description"),
            ('---\nname: sample-skill\ndescription: "Sample"\n---\n', "instructions"),
        ):
            with self.subTest(message=message):
                self.write("sample-skill/SKILL.md", source)
                with self.assertRaisesRegex(ValueError, message):
                    self.package()

    def test_rejects_ui_metadata_missing_required_fields(self):
        self.write("sample-skill/agents/openai.yaml", "interface:\n  display_name: Sample\n")
        with self.assertRaisesRegex(ValueError, "short_description"):
            self.package()

    def test_rejects_default_prompt_without_skill_invocation(self):
        path = self.root / "sample-skill/agents/openai.yaml"
        path.write_text(path.read_text().replace("$sample-skill", "sample-skill"))
        with self.assertRaisesRegex(ValueError, "default_prompt must mention"):
            self.package()

    def test_rejects_untracked_ui_metadata(self):
        subprocess.run(["git", "rm", "--cached", "-q", "sample-skill/agents/openai.yaml"],
                       cwd=self.root, check=True)
        with self.assertRaisesRegex(ValueError, "missing tracked UI metadata"):
            self.package()

    def test_rejects_missing_or_untracked_link_target(self):
        path = self.root / "sample-skill/references/example.md"
        path.unlink()
        with self.assertRaisesRegex(ValueError, "regular tracked file"):
            self.package()
        self.track()
        path.write_text("untracked reference\n")
        with self.assertRaisesRegex(ValueError, "link missing from package"):
            self.package()

    def test_rejects_links_outside_repository(self):
        self.write("sample-skill/references/example.md", "Read [outside](../../../outside.md).\n")
        with self.assertRaisesRegex(ValueError, "link escapes repository"):
            self.package()

    def test_rejects_repository_without_skills(self):
        subprocess.run(["git", "rm", "--cached", "-q", "sample-skill/SKILL.md"],
                       cwd=self.root, check=True)
        with self.assertRaisesRegex(ValueError, "No tracked skill"):
            self.package()


if __name__ == "__main__":
    unittest.main()
