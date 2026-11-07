#!/usr/bin/env python3
"""Static validation of the Retro OS theme bundle. Requires PyYAML."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from build import ORDER

class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'Duplicate YAML key: {key!r} (line {key_node.start_mark.line+1})')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def read(path):
    doc = yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueKeyLoader)
    if not isinstance(doc, dict) or not doc:
        raise ValueError(f'{path}: expected non-empty mapping')
    for theme_name, values in doc.items():
        if not isinstance(theme_name, str) or not isinstance(values, dict) or not values:
            raise ValueError(f'{path}: invalid theme {theme_name!r}')
        for key, value in values.items():
            if key == 'modes':
                if not isinstance(value, dict) or not set(value).issubset({'light','dark'}):
                    raise ValueError(f'{path}: invalid modes')
                for mode, mode_values in value.items():
                    if not isinstance(mode_values, dict) or any(not isinstance(v, str) for v in mode_values.values()):
                        raise ValueError(f'{path}: mode values must be strings')
            elif not isinstance(key, str) or not isinstance(value, str):
                raise ValueError(f'{path}: expected quoted string value for {theme_name}.{key}')
    return doc


def main():
    expected = {}
    for name in ORDER:
        path = ROOT / 'source' / name
        individual = read(path)
        for k,v in individual.items():
            if k in expected:
                raise ValueError(f'duplicate theme {k}')
            expected[k] = v
    merged = read(ROOT / 'themes' / 'retro_os_collection.yaml')
    if merged != expected:
        raise ValueError('Compiled themes do not match the source themes!')
    print(f'Valid: {len(merged)} themes, all values strings, no duplicate keys, no unsupported tags.')
    for name in merged:
        print(' -',name)


if __name__ == '__main__':
    main()
