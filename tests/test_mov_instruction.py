import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestSubInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_sub_r4_equals_r6_minus_r1(self):
        self.cpu.regs[6] = 20  # rs = R6
        self.cpu.regs[1] = 5   # rt = R1

        # opcode=2 (SUB), rd=4, rs=6, rt=1 => 0010 0100 0110 0001 = 0x2461
        self.mem.write16(0x0100, 0x2461)

        self.cpu.step()

        self.assertEqual(self.cpu.regs[4], 15)
        self.assertEqual(self.cpu.pc, 0x0102)

if __name__ == '__main__':
    unittest.main()
