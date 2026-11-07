#!/usr/bin/env python3
"""Build the single installable theme bundle from the preserved originals.

Run: python tools/build.py
Check: python tools/build.py --check
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ORDER = ['windows_31_program_manager.yaml', 'windows_95_classic.yaml', 'windows_98_classic.yaml', 'windows_nt_40_workstation.yaml', 'windows_2000_classic.yaml', 'windows_xp_luna.yaml', 'macintosh_system_6_monochrome.yaml', 'macos_system_7_classic.yaml', 'macos_8_platinum.yaml', 'macos_9_platinum.yaml', 'macos_x_10_cheetah_aqua.yaml', 'os2_warp_4_merlin.yaml', 'amiga_workbench_2x.yaml', 'solaris_cde_motif.yaml', 'beos_r5_tracker.yaml', 'apple_lisa_office_system.yaml']
OUTPUT = ROOT / 'themes' / 'retro_os_collection.yaml'


def render():
    parts = [
        '# Retro OS Themes — Home Assistant Edition\n',
        '# GENERATED FILE. Edit source/*.yaml, then run python tools/build.py.\n',
        '# One installable YAML, sixteen separately selectable theme names.\n',
        '# No custom tags, external images or custom integrations required.\n\n',
    ]
    for filename in ORDER:
        path = ROOT / 'source' / filename
        text = path.read_text(encoding='utf-8').rstrip() + '\n'
        parts.append('\n# ' + '=' * 69 + '\n')
        parts.append('# Source: ' + filename + '\n')
        parts.append('# ' + '=' * 69 + '\n\n')
        parts.append(text)
    return ''.join(parts)


def main():
    contents = render()
    if '--check' in sys.argv:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding='utf-8') != contents:
            print('Theme bundle is out of date. Run: python tools/build.py', file=sys.stderr)
            raise SystemExit(1)
        print('Theme bundle is up to date.')
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(contents, encoding='utf-8')
        print('Wrote', OUTPUT)


if __name__ == '__main__':
    main()
