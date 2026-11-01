#!/usr/bin/env python3
"""Split multichar letter symbols (x̌, q̓, k̓ʷ, ...) into single codepoints.

Usage: split-multichar-arcs.py split-composed-chars.regex IN.hfst OUT.hfst

The letter+diacritic combinations must stay single symbols through lexc and
twolc, since reduplication copies consonants 1 and 3 as whole units. Only the
finished raw fst is split here.

Composing split-composed-chars on both sides of the fst gives the same
strings, but every split letter on the lexical side can then be aligned in
two ways (x ̌:̌  vs  x 0:̌ ̌:0), i.e. 2^n identical analyses for a lemma with n
such letters. Instead, every arc carrying a multichar letter is replaced
with an aligned codepoint sequence using hfst-substitute:
    x̌:x̌ -> x ̌      0:x̌ -> 0:x 0:̌      x̌:0 -> x:0 ̌:0
"""

import re
import shutil
import subprocess
import sys
import tempfile

EPS = '@0@'
FORMATS = {'foma': 'foma', 'OpenFST': 'openfst-tropical', 'SFST': 'sfst'}


def run(*args):
    return subprocess.run(args, check=True, capture_output=True,
                          text=True).stdout


def read_split_regex(path):
    """Map each multichar letter to its list of codepoint symbols."""
    split = {}
    with open(path, encoding='utf-8') as regex:
        for line in regex:
            m = re.match(r'\s*"([^"]+)"\s*->\s*((?:\{[^}]*\})+)', line)
            if m:
                split[m.group(1)] = re.findall(r'\{([^}]*)\}', m.group(2))
    return split


def main(regex, fst_in, fst_out):
    split = read_split_regex(regex)
    fst_type = re.search(r'fst type: (\S+)', run('hfst-summarize', fst_in))
    fmt = FORMATS[fst_type.group(1)]

    pairs = set()
    for line in run('hfst-fst2txt', fst_in).splitlines():
        f = line.split('\t')
        if len(f) >= 4 and (f[2] in split or f[3] in split):
            pairs.add((f[2], f[3]))

    tmpdir = tempfile.mkdtemp()
    try:
        cur = fst_in
        for n, (a, b) in enumerate(sorted(pairs)):
            upper = split.get(a, [] if a == EPS else [a])
            lower = split.get(b, [] if b == EPS else [b])
            k = max(len(upper), len(lower))
            upper += [EPS] * (k - len(upper))
            lower += [EPS] * (k - len(lower))
            att = f'{tmpdir}/r{n}.att'
            with open(att, 'w', encoding='utf-8') as out:
                for i, (x, y) in enumerate(zip(upper, lower)):
                    out.write(f'{i}\t{i+1}\t{x}\t{y}\n')
                out.write(f'{k}\n')
            run('hfst-txt2fst', '-f', fmt, att, '-o', att + '.hfst')
            nxt = f'{tmpdir}/s{n}.hfst'
            run('hfst-substitute', '-i', cur, '-o', nxt,
                '-f', f'{a}:{b}', '-T', att + '.hfst')
            cur = nxt
        run('hfst-minimize', '-i', cur, '-o', fst_out)
    finally:
        shutil.rmtree(tmpdir)
    print(f'{fst_out}: split {len(pairs)} multichar symbol pairs',
          file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
