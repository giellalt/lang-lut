#!/usr/bin/env python3
"""Generate with a reversed generator (src/fst/rev-generator-gt-*.hfstol).

Usage: rev-generate.py [REV_GENERATOR.hfstol] < analyses

Reads one analysis per line (lemma+Tag+Tag...), reverses it (tags as units,
lemma by codepoint), looks it up in the reversed generator and prints
"analysis<TAB>wordform" lines in the usual hfst-lookup layout.
"""

import os
import re
import subprocess
import sys

DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '..', 'src', 'fst', 'rev-generator-gt-norm.hfstol')


def reverse_analysis(analysis):
    i = analysis.find('+')
    lemma, tags = (analysis, '') if i < 0 else (analysis[:i], analysis[i:])
    return ''.join(reversed(re.findall(r'\+[^+]+', tags))) + lemma[::-1]


def main():
    fst = sys.argv[1] if len(sys.argv) > 1 else DEFAULT
    analyses = [l.strip() for l in sys.stdin if l.strip()]
    back = {reverse_analysis(a): a for a in analyses}
    out = subprocess.run(['hfst-lookup', '-q', fst],
                         input='\n'.join(back) + '\n',
                         capture_output=True, text=True, check=True).stdout
    results = {}
    for line in out.splitlines():
        f = line.split('\t')
        if len(f) >= 2 and f[0] in back:
            form = back[f[0]] + '+?' if f[1].endswith('+?') else f[1][::-1]
            results.setdefault(back[f[0]], []).append(
                (form, f[2] if len(f) > 2 else ''))
    for a in analyses:
        seen = set()
        for form, weight in results.get(a, [(a + '+?', 'inf')]):
            if form not in seen:
                seen.add(form)
                print(f'{a}\t{form}\t{weight}')
        print()


if __name__ == '__main__':
    main()
