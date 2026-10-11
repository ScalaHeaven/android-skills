#!/usr/bin/env python3
"""Check an explicit JSON module dependency adjacency map for cycles."""
import argparse
import json
from pathlib import Path


def analyze(graph):
    if not isinstance(graph, dict) or not all(isinstance(k, str) and isinstance(v, list) and all(isinstance(x, str) for x in v) for k,v in graph.items()):
        raise ValueError('Expected an object mapping module names to lists of dependency names')
    unknown = sorted({v for values in graph.values() for v in values} - set(graph))
    state, order, cycles = {}, [], []
    def visit(node, stack):
        if state.get(node) == 1:
            cycles.append(stack[stack.index(node):] + [node])
            return
        if state.get(node) == 2:
            return
        state[node] = 1
        for child in sorted(set(graph.get(node, []))):
            visit(child, stack+[node])
        state[node] = 2
        order.append(node)
    for node in sorted(graph):
        visit(node, [])
    return {'cycles':cycles, 'undeclared_nodes':unknown, 'dependency_first_order':None if cycles else order,
            'limitations':['Only provided edges are checked; resolve variants and dynamic Gradle dependencies separately.']}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('graph', type=Path)
    args = parser.parse_args()
    try:
        result = analyze(json.loads(args.graph.read_text(encoding='utf-8')))
        print(json.dumps(result, indent=2))
        return 1 if result['cycles'] or result['undeclared_nodes'] else 0
    except (OSError, ValueError, RecursionError) as error:
        parser.exit(2, f'error: {error}\n')

if __name__ == '__main__':
    raise SystemExit(main())
