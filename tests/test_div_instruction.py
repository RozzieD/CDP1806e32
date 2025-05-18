import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestDivInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_div_r4_equals_r6_div_r2(self):
        self.cpu.regs[6] = 84
        self.cpu.regs[2] = 7
        # opcode = 0xB (DIV), rd = 4, rs = 6, rt = 2 => 0xB462
        self.mem.write16(0x0100, 0xB462)
        self.cpu.step()
        self.assertEqual(self.cpu.regs[4], 12)

    def test_div_by_zero_raises(self):
        self.cpu.regs[1] = 123
        self.cpu.regs[0] = 0
        self.mem.write16(0x0100, 0xB210)  # DIV R2, R1, R0
        with self.assertRaises(ZeroDivisionError):
            self.cpu.step()

if __name__ == '__main__':
    unittest.main()
