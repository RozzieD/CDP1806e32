import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestLDIInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_ldi_r5_with_imm16(self):
        # LDI R5, 0xBEEF
        # First word: 0x9305 (opcode=0x93, reg=5)
        # Second word: 0xBEEF (immediate value)
        self.mem.write16(0x0100, 0x9305)
        self.mem.write16(0x0102, 0xBEEF)

        self.cpu.step()

        self.assertEqual(self.cpu.regs[5], 0xBEEF)
        self.assertEqual(self.cpu.pc, 0x0104)

if __name__ == '__main__':
    unittest.main()
