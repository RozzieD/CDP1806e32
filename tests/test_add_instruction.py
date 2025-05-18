import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestAddInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_add_r2_equals_r3_plus_r0(self):
        self.cpu.regs[3] = 7  # rs = R3
        self.cpu.regs[0] = 5  # rt = R0

        # opcode=1 (ADD), rd=2, rs=3, rt=0 => 0001 0010 0011 0000 = 0x1230
        self.mem.write16(0x0100, 0x1230)

        self.cpu.step()

        self.assertEqual(self.cpu.regs[2], 12)
        self.assertEqual(self.cpu.pc, 0x0102)

if __name__ == '__main__':
    unittest.main()
