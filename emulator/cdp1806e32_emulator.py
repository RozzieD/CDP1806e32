# cdp1806e32_emulator.py - Enhanced Emulator with Disassembler and UART simulation

from irq_emulator_hook import IRQController, MockMemory

class CPU:
    def __init__(self, memory):
        self.regs = [0] * 16
        self.pc = 0
        self.memory = memory
        self.running = True

    def fetch(self):
        instr = self.memory.read16(self.pc)
        self.pc += 2
        return instr

    def disasm(self, instr):
        opcode = (instr >> 12) & 0xF
        rd = (instr >> 8) & 0xF
        rs = (instr >> 4) & 0xF
        imm4 = instr & 0xF
        opnames = ["NOP", "ADD", "SUB", "MOV", "LD", "ST", "JMP", "TRAP"]
        return f"{opnames[opcode] if opcode < len(opnames) else '???'} R{rd}, R{rs}, {imm4}"

    def step(self):
        instr = self.fetch()
        print(f"PC={self.pc - 2:04X}  INST={instr:04X}  {self.disasm(instr)}")
        opcode = (instr >> 12) & 0xF
        rd = (instr >> 8) & 0xF
        rs = (instr >> 4) & 0xF
        imm4 = instr & 0xF

        if instr == 0x0000:
            return  # NOP

        if opcode == 0x1:  # ADD
            self.regs[rd] = (self.regs[rs] + self.regs[imm4]) & 0xFFFFFFFF
        elif opcode == 0x2:  # SUB
            self.regs[rd] = (self.regs[rs] - self.regs[imm4]) & 0xFFFFFFFF
        elif opcode == 0x3:  # MOV
            self.regs[rd] = self.regs[rs]
        elif opcode == 0x4:  # LD
            addr = (self.regs[rs] + imm4) & 0xFFFF
            self.regs[rd] = self.memory.read16(addr)
        elif opcode == 0x5:  # ST
            addr = (self.regs[rs] + imm4) & 0xFFFF
            self.memory.write16(addr, self.regs[rd])
        elif opcode == 0x6:  # JMP
            self.pc = self.regs[rd] & 0xFFFF
        elif opcode == 0x7:  # TRAP
            print("[TRAP] Trap called")
            self.running = False
        else:
            print(f"Unknown opcode {opcode:X} at PC={self.pc - 2:04X}")
            self.running = False

    def run(self, steps=1000):
        for _ in range(steps):
            if not self.running:
                break
            self.step()

if __name__ == "__main__":
    mem = MockMemory()
    irq = IRQController(mem)
    cpu = CPU(mem)

    # Program: UART echo on interrupt simulation
    # 0x0000: li r0, 0x42  (simulate write)
    mem.write16(0x0000, 0x7000)  # TRAP

    mem.write16(0xFF02, 2000)    # Timer interval
    mem.write8(0xFF03, 0x03)     # Timer enable + IRQ enable
    mem.write8(0xFF06, 0x00)     # Clear IRQ

    cpu.pc = 0x0000

    while cpu.running:
        cpu.step()
        irq.step()
        irq.acknowledge()
# cdp1806e32_emulator.py - Enhanced Emulator with Disassembler and UART simulation

from irq_emulator_hook import IRQController, MockMemory

class CPU:
    def __init__(self, memory):
        self.regs = [0] * 16
        self.pc = 0
        self.memory = memory
        self.running = True

    def fetch(self):
        instr = self.memory.read16(self.pc)
        self.pc += 2
        return instr

    def disasm(self, instr):
        opcode = (instr >> 12) & 0xF
        rd = (instr >> 8) & 0xF
        rs = (instr >> 4) & 0xF
        imm4 = instr & 0xF
        opnames = ["NOP", "ADD", "SUB", "MOV", "LD", "ST", "JMP", "TRAP"]
        return f"{opnames[opcode] if opcode < len(opnames) else '???'} R{rd}, R{rs}, {imm4}"

    def step(self):
        instr = self.fetch()
        print(f"PC={self.pc - 2:04X}  INST={instr:04X}  {self.disasm(instr)}")
        opcode = (instr >> 12) & 0xF
        rd = (instr >> 8) & 0xF
        rs = (instr >> 4) & 0xF
        imm4 = instr & 0xF

        if instr == 0x0000:
            return  # NOP

        if opcode == 0x1:  # ADD
            self.regs[rd] = (self.regs[rs] + self.regs[imm4]) & 0xFFFFFFFF
        elif opcode == 0x2:  # SUB
            self.regs[rd] = (self.regs[rs] - self.regs[imm4]) & 0xFFFFFFFF
        elif opcode == 0x3:  # MOV
            self.regs[rd] = self.regs[rs]
        elif opcode == 0x4:  # LD
            addr = (self.regs[rs] + imm4) & 0xFFFF
            self.regs[rd] = self.memory.read16(addr)
        elif opcode == 0x5:  # ST
            addr = (self.regs[rs] + imm4) & 0xFFFF
            self.memory.write16(addr, self.regs[rd])
        elif opcode == 0x6:  # JMP
            self.pc = self.regs[rd] & 0xFFFF
        elif opcode == 0x7:  # TRAP
            print("[TRAP] Trap called")
            self.running = False
        else:
            print(f"Unknown opcode {opcode:X} at PC={self.pc - 2:04X}")
            self.running = False

    def run(self, steps=1000):
        for _ in range(steps):
            if not self.running:
                break
            self.step()

if __name__ == "__main__":
    mem = MockMemory()
    irq = IRQController(mem)
    cpu = CPU(mem)

    # Program: UART echo on interrupt simulation
    # 0x0000: li r0, 0x42  (simulate write)
    mem.write16(0x0000, 0x7000)  # TRAP

    mem.write16(0xFF02, 2000)    # Timer interval
    mem.write8(0xFF03, 0x03)     # Timer enable + IRQ enable
    mem.write8(0xFF06, 0x00)     # Clear IRQ

    cpu.pc = 0x0000

    while cpu.running:
        cpu.step()
        irq.step()
        irq.acknowledge()
