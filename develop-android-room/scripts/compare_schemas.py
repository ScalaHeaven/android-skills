#!/usr/bin/env python3
"""Compare exported Room schemas structurally; this does not validate a migration."""
import argparse
import json
from pathlib import Path

def database(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('database'), dict):
        raise ValueError('Expected a Room export with a database object')
    db = data['database']
    if not isinstance(db.get('entities'), list) or not all(isinstance(e, dict) and isinstance(e.get('tableName'), str) for e in db['entities']):
        raise ValueError('Expected Room entities with tableName')
    names = [e['tableName'] for e in db['entities']]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate table names')
    return db

def compare(before, after):
    a = {e['tableName']:e for e in before['entities']}
    b = {e['tableName']:e for e in after['entities']}
    changed = []
    for name in sorted(a.keys() & b.keys()):
        keys = sorted(k for k in a[name].keys() | b[name].keys() if a[name].get(k) != b[name].get(k))
        if keys:
            changed.append({'table':name, 'changed_sections':keys})
    return {'before_version':before.get('version'), 'after_version':after.get('version'),
            'added_tables':sorted(b.keys()-a.keys()), 'removed_tables':sorted(a.keys()-b.keys()), 'changed_tables':changed,
            'views_changed':before.get('views', []) != after.get('views', []),
            'limitations':['Structural inventory only; run migrations on populated old schemas and assert values, constraints and indexes.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path)
    parser.add_argument('after', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(compare(database(args.before), database(args.after)), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, f'error: {error}\n')

if __name__ == '__main__':
    main()
