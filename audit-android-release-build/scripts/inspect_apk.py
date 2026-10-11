#!/usr/bin/env python3
"""Inventory an APK/AAB ZIP. Does not prove signing or ELF/load compatibility."""
import argparse
import json
import re
import zipfile
from collections import Counter
from pathlib import Path


def inspect(path):
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        counts = Counter(e.filename for e in entries)
        native = []
        for entry in entries:
            match = re.search(r'(?:^|/)lib/([^/]+)/([^/]+\.so)$', entry.filename)
            if match:
                native.append({'path':entry.filename, 'abi':match.group(1), 'library':match.group(2), 'bytes':entry.file_size, 'compression_method':entry.compress_type})
        return {'entries':len(entries), 'uncompressed_bytes':sum(e.file_size for e in entries), 'native_libraries':native,
                'abis':sorted({e['abi'] for e in native}),
                'duplicate_paths':sorted(name for name,count in counts.items() if count > 1),
                'limitations':['No extraction is performed.', 'Verify signing with supported Android tools and ELF/page-size/ZIP alignment with the relevant tooling.', 'An AAB inventory does not establish which split APKs are delivered to a device.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.artifact), indent=2))
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.exit(2, f'error: {error}\n')

if __name__ == '__main__':
    main()
