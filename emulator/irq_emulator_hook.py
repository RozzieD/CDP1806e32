# irq_emulator_hook.py - Emulated interrupt trigger for CDP1806E-R32

import time

class IRQController:
    def __init__(self, memory):
        self.memory = memory
        self.irq_ack = 0xFF07
        self.irq_status = 0xFF06
        self.timer_counter = 0
        self.timer_target = 2000
        self.timer_enabled = False

    def step(self):
        ctrl = self.memory.read8(0xFF03)
        val = self.memory.read16(0xFF02)

        if ctrl & 0x01:  # Timer enabled
            self.timer_counter += 1
            if self.timer_counter >= self.timer_target:
                self.memory.write8(self.irq_status, self.memory.read8(self.irq_status) | 0x01)
                self.timer_counter = 0

    def acknowledge(self):
        ack = self.memory.read8(self.irq_ack)
        if ack & 0x01:
            self.memory.write8(self.irq_status, self.memory.read8(self.irq_status) & ~0x01)
        if ack & 0x02:
            self.memory.write8(self.irq_status, self.memory.read8(self.irq_status) & ~0x02)
        self.memory.write8(self.irq_ack, 0)

class MockMemory:
    def __init__(self):
        self.mem = [0] * 0x10000

    def read8(self, addr):
        return self.mem[addr]

    def write8(self, addr, val):
        self.mem[addr] = val & 0xFF

    def read16(self, addr):
        return self.mem[addr] | (self.mem[addr + 1] << 8)

    def write16(self, addr, val):
        self.mem[addr] = val & 0xFF
        self.mem[addr + 1] = (val >> 8) & 0xFF

if __name__ == "__main__":
    mem = MockMemory()
    irq = IRQController(mem)

    mem.write16(0xFF02, 2000)
    mem.write8(0xFF03, 0x03)

    for _ in range(10000):
        irq.step()
        irq.acknowledge()
        if mem.read8(0xFF06) & 0x01:
            print("[IRQ] Timer interrupt triggered")
            time.sleep(0.1)
