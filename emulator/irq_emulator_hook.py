# emulator/irq_emulator_hook.py

class MockMemory:
    def __init__(self):
        self.mem = {}

    def read16(self, addr):
        hi = self.mem.get(addr, 0)
        lo = self.mem.get(addr + 1, 0)
        return (hi << 8) | lo

    def write16(self, addr, value):
        self.mem[addr] = (value >> 8) & 0xFF
        self.mem[addr + 1] = value & 0xFF

    def read32(self, addr):
        return (
            (self.mem.get(addr, 0) << 24) |
            (self.mem.get(addr + 1, 0) << 16) |
            (self.mem.get(addr + 2, 0) << 8) |
            self.mem.get(addr + 3, 0)
        )

    def write32(self, addr, value):
        self.mem[addr] = (value >> 24) & 0xFF
        self.mem[addr + 1] = (value >> 16) & 0xFF
        self.mem[addr + 2] = (value >> 8) & 0xFF
        self.mem[addr + 3] = value & 0xFF
