#!/usr/bin/env python3
# PNPMD v1.02 preprocessor: header ' #slug' -> '{#sec:slug}', inline '@slug' -> '[@sec:slug]'

import re, sys, io

header_re = re.compile(r"^(#{1,6}\s+.*?)(\s+)#([A-Za-z0-9_-]+)\s*$")
ref_re    = re.compile(r"(^|[^@\w])@([A-Za-z0-9_-]+)")

def conv_header(line: str) -> str:
    m = header_re.match(line)
    if not m: return line
    before, sp, slug = m.groups()
    return f"{before}{sp}" + "{#sec:" + slug + "}"

def conv_refs(text: str) -> str:
    def repl(m):
        lead = m.group(1)
        slug = m.group(2)
        return f"{lead}[@sec:{slug}]"
    return ref_re.sub(repl, text)

def main():
    if len(sys.argv) >= 2:
        src = open(sys.argv[1], "r", encoding="utf-8").read()
    else:
        src = sys.stdin.read()
    lines = [conv_header(ln) for ln in src.splitlines()]
    out = "\n".join(lines)
    out = conv_refs(out)
    sys.stdout.write(out)

if __name__ == "__main__":
    main()
