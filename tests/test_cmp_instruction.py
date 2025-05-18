import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestCmpInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_cmp_equal_sets_zero(self):
        self.cpu.regs[2] = 42
        self.cpu.regs[3] = 42
        # CMP R2, R3 -> opcode=0xD, rs=2, rt=3 => 1101 0000 0010 0011 = 0xD023
        self.mem.write16(0x0100, 0xD023)
        self.cpu.step()
        self.assertEqual(self.cpu.flag_z, 1)
        self.assertEqual(self.cpu.flag_n, 0)

    def test_cmp_less_sets_negative(self):
        self.cpu.regs[4] = 10
        self.cpu.regs[5] = 50
        self.mem.write16(0x0100, 0xD045)  # CMP R4, R5
        self.cpu.step()
        self.assertEqual(self.cpu.flag_z, 0)
        self.assertEqual(self.cpu.flag_n, 1)

if __name__ == '__main__':
    unittest.main()
# This test suite tests the CMP instruction of the CPU.
# It checks the zero and negative flags after comparing two registers.