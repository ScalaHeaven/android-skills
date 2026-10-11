#!/usr/bin/env python3
"""Read-only hints from Android build files; never execute Gradle or print secrets."""
import argparse
import json
import os
import re
from pathlib import Path

SKIP = {'.git', '.gradle', 'build', '.idea', 'node_modules', '.cxx'}
PATTERN = re.compile(r'\b(minSdk|targetSdk|compileSdk)(?:Version)?\s*(?:=\s*|\(?\s*)(\d+)\b')

def inspect(root):
    if not root.is_dir():
        raise ValueError('Project directory does not exist')
    files = []
    for directory, folders, filenames in os.walk(root, followlinks=False):
        folders[:] = sorted(f for f in folders if f not in SKIP and not (Path(directory)/f).is_symlink())
        for filename in sorted(filenames):
            path = Path(directory)/filename
            if path.is_symlink() or filename not in {'build.gradle', 'build.gradle.kts', 'settings.gradle', 'settings.gradle.kts', 'libs.versions.toml', 'gradle-wrapper.properties'}:
                continue
            relative = path.relative_to(root)
            hints = []
            if path.name.startswith('build.gradle'):
                for number, line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
                    if line.lstrip().startswith(('//', '*')):
                        continue
                    for key, value in PATTERN.findall(line):
                        hints.append({'line':number, 'key':key, 'literal_value':int(value)})
            files.append({'path':relative.as_posix(), 'sdk_hints':hints})
    return {'files':files, 'limitations':['Text hints only; convention plugins, variables and resolved Gradle configuration are not evaluated.', 'File contents, credentials and endpoints are not printed.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.project.resolve()), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, f'error: {error}\n')

if __name__ == '__main__':
    main()
