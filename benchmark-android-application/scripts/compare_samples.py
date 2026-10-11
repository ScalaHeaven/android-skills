#!/usr/bin/env python3
"""Compare normalized benchmark samples descriptively; no significance inference."""
import argparse
import json
import math
import statistics
from pathlib import Path

def load(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('metric'), str) or not isinstance(data.get('unit'), str):
        raise ValueError('Expected metric, unit, samples and optional context')
    values = data.get('samples')
    if not isinstance(values, list) or not values or not all(isinstance(x, (int,float)) and not isinstance(x,bool) and math.isfinite(x) and x >= 0 for x in values):
        raise ValueError('samples must be a nonempty list of finite nonnegative numbers')
    return data

def compare(before, after):
    if (before['metric'],before['unit']) != (after['metric'],after['unit']):
        raise ValueError('Metric and unit must match')
    def summary(data):
        values = data['samples']
        return {'count':len(values), 'median':statistics.median(values), 'min':min(values), 'max':max(values)}
    a, b = summary(before), summary(after)
    return {'metric':before['metric'], 'unit':before['unit'], 'before':a, 'after':b,
            'median_change_percent':None if a['median'] == 0 else (b['median']/a['median']-1)*100,
            'contexts_match':before.get('context') == after.get('context'),
            'context_recorded':bool(before.get('context')) and bool(after.get('context')),
            'limitations':['Descriptive comparison only; inspect raw results, variability and matched experimental conditions.', 'Positive change means a larger value, not necessarily a regression; direction depends on the metric.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path)
    parser.add_argument('after', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(compare(load(args.before), load(args.after)), indent=2))
    except (OSError, ValueError, OverflowError) as error:
        parser.exit(2, f'error: {error}\n')

if __name__ == '__main__':
    main()
