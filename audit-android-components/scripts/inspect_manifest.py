#!/usr/bin/env python3
"""Summarize a text Android manifest. Output is inventory, not vulnerability proof."""
import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

NS = '{http://schemas.android.com/apk/res/android}'

def inspect(path):
    root = ET.parse(path).getroot()
    if root.tag != 'manifest':
        raise ValueError('Expected a text manifest XML root')
    app = root.find('application')
    components = []
    if app is not None:
        for item in app:
            if item.tag not in {'activity', 'activity-alias', 'service', 'receiver', 'provider'}:
                continue
            filters = item.findall('intent-filter')
            components.append({
                'type':item.tag,
                'name':item.get(NS+'name'),
                'exported_declared':item.get(NS+'exported'),
                'permission':item.get(NS+'permission', app.get(NS+'permission')),
                'read_permission':item.get(NS+'readPermission'),
                'write_permission':item.get(NS+'writePermission'),
                'authorities':item.get(NS+'authorities'),
                'grant_uri_permissions':item.get(NS+'grantUriPermissions'),
                'intent_filter_count':len(filters),
                'actions':[action.get(NS+'name') for f in filters for action in f.findall('action')],
            })
    return {'package':root.get('package'), 'permissions':[p.get(NS+'name') for p in root.findall('uses-permission')],
            'application':{} if app is None else {k:app.get(NS+k) for k in ['debuggable', 'allowBackup', 'usesCleartextTraffic', 'networkSecurityConfig']},
            'components':components,
            'limitations':['Use the merged release text manifest for delivery review.', 'No defaults or caller authorization are inferred; exported status alone is not a vulnerability.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(inspect(args.manifest), indent=2))
    except (OSError, ValueError, ET.ParseError) as error:
        parser.exit(2, f'error: {error}\n')

if __name__ == '__main__':
    main()
