# Tiny assembler: converts .asm to .hex16 (16-bit opcodes only)

mnemonics = {
    'LDI':   lambda r, v: [0x9300 | int(r[1]), int(v, 0)],
    'MUL':   lambda rd, rs, rt: [0xA000 | (int(rd[1]) << 8) | (int(rs[1]) << 4) | int(rt[1])],
    'PUSH':  lambda r: [0xB000 | int(r[1])],
    'POP':   lambda r: [0xB100 | int(r[1])],
    'TRAP':  lambda: [0xE000],
}

def assemble_line(line):
    line = line.split(';')[0].strip()  # strip inline comments
    if not line:
        return []
    parts = line.split()
    if not parts:
        return []
    op = parts[0].upper()
    args = [a.strip(',') for a in parts[1:]]
    return mnemonics[op](*args)


def assemble_file(path):
    hexlines = []
    with open(path) as f:
        for line in f:
            codes = assemble_line(line)
            for code in codes:
                hexlines.append(f"{code:04X}")
    return hexlines

if __name__ == "__main__":
    import sys
    out = assemble_file(sys.argv[1])
    for line in out:
        print(line)
