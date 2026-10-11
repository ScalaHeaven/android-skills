#!/usr/bin/env python3
"""Summarize JUnit-style test cases without printing failure messages or secrets."""
import argparse
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path

def summarize(paths):
    counts = {'passed':0, 'failed':0, 'errored':0, 'skipped':0}
    cases, invalid = [], []
    for path in paths:
        try:
            file_cases = []
            root = ET.parse(path).getroot()
            if root.tag not in {'testsuite', 'testsuites'}:
                raise ValueError('Not a JUnit report')
            for case in root.iter('testcase'):
                duration = float(case.get('time', '0'))
                if not math.isfinite(duration) or duration < 0:
                    raise ValueError('Invalid testcase time')
                status = ('errored' if case.find('error') is not None else 'failed' if case.find('failure') is not None else 'skipped' if case.find('skipped') is not None else 'passed')
                file_cases.append({'report':str(path), 'class':case.get('classname'), 'name':case.get('name'), 'seconds':duration, 'status':status})
            cases.extend(file_cases)
        except (OSError, ValueError, ET.ParseError) as error:
            invalid.append({'report':str(path), 'error':str(error)})
    for case in cases:
        counts[case['status']] += 1
    return {'counts':counts, 'test_cases':len(cases), 'slowest':sorted(cases, key=lambda c:c['seconds'], reverse=True)[:10],
            'invalid_reports':invalid, 'limitations':['Counts represent reported executions, not unique tests or historical flakiness.', 'Retries and repeated runs are counted separately; aggregate suite counters are not trusted.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reports', nargs='+', type=Path)
    args = parser.parse_args()
    paths = []
    for path in args.reports:
        paths.extend(sorted(path.rglob('*.xml')) if path.is_dir() else [path])
    result = summarize(sorted(set(paths)))
    print(json.dumps(result, indent=2))
    return 2 if result['invalid_reports'] or result['test_cases'] == 0 else 1 if result['counts']['failed'] or result['counts']['errored'] else 0

if __name__ == '__main__':
    raise SystemExit(main())
