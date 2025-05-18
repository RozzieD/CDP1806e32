#class CPU:
    def __init__(self, mem):
        self.mem = mem
        self.regs = [0] * 16  # R0–R15
        self.pc = 0x0000
        self.halted = False

    def fetch(self):
        instr = self.mem.read16(self.pc)
        self.pc = (self.pc + 2) & 0xFFFF
        return instr

    def step(self):
        instr = self.fetch()
        opcode = (instr >> 12) & 0xF
        rd = (instr >> 8) & 0xF
        rs = (instr >> 4) & 0xF
        rt = instr & 0xF

        if opcode == 0x0:  # NOP
            pass

        elif opcode == 0x1:  # ADD
            self.regs[rd] = (self.regs[rs] + self.regs[rt]) & 0xFFFFFFFF

        elif opcode == 0x2:  # SUB
            self.regs[rd] = (self.regs[rs] - self.regs[rt]) & 0xFFFFFFFF

        elif opcode == 0x3:  # MOV
            self.regs[rd] = self.regs[rs]

        elif opcode == 0x4:  # AND
            self.regs[rd] = self.regs[rs] & self.regs[rt]

        elif opcode == 0x5:  # OR
            self.regs[rd] = self.regs[rs] | self.regs[rt]

        elif opcode == 0x6:  # XOR
            self.regs[rd] = self.regs[rs] ^ self.regs[rt]

        elif opcode == 0x7:  # LD
            addr = (self.regs[rs] + rt) & 0xFFFF
            self.regs[rd] = self.mem.read32(addr)

        elif opcode == 0x8:  # ST
            addr = (self.regs[rs] + rt) & 0xFFFF
            self.mem.write32(addr, self.regs[rd])

        elif opcode == 0x9:  # JMP
            self.pc = self.regs[rd] & 0xFFFF

        elif opcode == 0xF:  # RET
            self.pc = self.regs[15]  # Assume R15 is LR

        else:
            raise Exception(f"Unknown opcode: {opcode:04b}")
