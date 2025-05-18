class CPU:
    def __init__(self, mem):
        self.mem = mem
        self.regs = [0] * 16  # R0–R15
        self.pc = 0x0000
        self.halted = False
        self.flag_z = 0
        self.flag_n = 0

    def fetch(self):
        instr = self.mem.read16(self.pc)
        self.pc = (self.pc + 2) & 0xFFFF
        return instr

    def step(self):
        instr = self.fetch()
        print(f"PC={self.pc:04X} INSTR={instr:04X}")

        # Check for LDI imm16 format
        if (instr >> 8) == 0x93:
            reg = instr & 0xF
            imm = self.fetch()
            self.regs[reg] = imm
            return

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

        elif opcode == 0xA:  # MUL
            self.regs[rd] = (self.regs[rs] * self.regs[rt]) & 0xFFFFFFFF

        elif opcode == 0xB:
            subop = (instr >> 8) & 0xFF

            if subop == 0xB0:  # PUSH
                reg = instr & 0xF
                print(f"PUSH: R{reg} = {self.regs[reg]} --> [SP={self.regs[9]:04X}]")
                self.regs[9] = (self.regs[9] - 4) & 0xFFFF
                self.mem.write32(self.regs[9], self.regs[reg])

            elif subop == 0xB1:  # POP
                reg = instr & 0xF
                val = self.mem.read32(self.regs[9])
                print(f"POP: [SP={self.regs[9]:04X}] --> R{reg} = {self.regs[reg]}")
                self.regs[reg] = val
                self.regs[9] = (self.regs[9] + 4) & 0xFFFF

            elif (subop & 0xF0) == 0xB0:  # DIV
                rd = subop & 0x0F
                rs = (instr >> 4) & 0xF
                rt = instr & 0xF
                if self.regs[rt] == 0:
                    raise ZeroDivisionError("DIV by zero")
                self.regs[rd] = (self.regs[rs] // self.regs[rt]) & 0xFFFFFFFF

            else:
                raise Exception(f"Unknown 0xB subop: {subop:02X}")

        elif opcode == 0xD:  # CMP
            result = (self.regs[rs] - self.regs[rt]) & 0xFFFFFFFF
            self.flag_z = int(result == 0)
            self.flag_n = int((result >> 31) & 1)

        elif opcode == 0xC:  # Conditional Branch
            cond = (instr >> 8) & 0xF
            offset = instr & 0xFF
            if offset & 0x80:
                offset -= 0x100  # sign-extend
            branch = False
            if cond == 0x0 and self.flag_z == 1:  # BEQ
                branch = True
            elif cond == 0x1 and self.flag_z == 0:  # BNE
                branch = True
            elif cond == 0x2 and self.flag_n == 1:  # BLT
                branch = True
            elif cond == 0x3 and self.flag_n == 0:  # BGE
                branch = True
            if branch:
                self.pc = (self.pc + offset) & 0xFFFF

        elif instr == 0xC000:  # CALL (assume R10 = return address)
            self.regs[9] = (self.regs[9] - 4) & 0xFFFF
            self.mem.write32(self.regs[9], self.pc)
            self.pc = self.regs[10] & 0xFFFF

        elif instr == 0xF000:  # RET
            self.pc = self.mem.read32(self.regs[9]) & 0xFFFF
            self.regs[9] = (self.regs[9] + 4) & 0xFFFF

        elif opcode == 0xE:  # TRAP
            raise Exception("TRAP executed")

        else:
            raise Exception(f"Unknown opcode: {opcode:04b}")
