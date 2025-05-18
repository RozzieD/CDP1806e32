import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestMulInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_mul_r4_equals_r2_times_r3(self):
        self.cpu.regs[2] = 6
        self.cpu.regs[3] = 7
        # opcode = 0xA (MUL), rd = 4, rs = 2, rt = 3 => 0xA423
        self.mem.write16(0x0100, 0xA423)
        self.cpu.step()
        self.assertEqual(self.cpu.regs[4], 42)
        self.assertEqual(self.cpu.pc, 0x0102)

if __name__ == '__main__':
    unittest.main()
