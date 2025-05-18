class MockMemory:
    def __init__(self, size=0x10000):
        self.data = bytearray(size)

    def read8(self, addr):
        return self.data[addr & 0xFFFF]

    def read16(self, addr):
        hi = self.read8(addr)
        lo = self.read8(addr + 1)
        return (hi << 8) | lo

    def read32(self, addr):
        return (self.read16(addr) << 16) | self.read16(addr + 2)

    def write8(self, addr, value):
        self.data[addr & 0xFFFF] = value & 0xFF

    def write16(self, addr, value):
        self.write8(addr, (value >> 8) & 0xFF)
        self.write8(addr + 1, value & 0xFF)

    def write32(self, addr, value):
        self.write16(addr, (value >> 16) & 0xFFFF)
        self.write16(addr + 2, value & 0xFFFF)
