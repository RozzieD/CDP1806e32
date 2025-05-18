# tests/test_add_instruction.py

import unittest
from irq_emulator_hook import MockMemory
from cdp1806e32_emulator import CPU

class TestAddInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x100  # place test instruction in safe memory

    def test_add_r1_equals_r2_plus_r3(self):
        # Set register values
        self.cpu.regs[2] = 5
        self.cpu.regs[3] = 7

        # Encode ADD r1 = r2 + r3
        # opcode=0x1 (ADD), rd=1, rs=2, imm4=3 => 0x1230
        self.mem.write16(0x100, 0x1230)

        self.cpu.step()

        self.assertEqual(self.cpu.regs[1], 12)
        self.assertEqual(self.cpu.pc, 0x102)

if __name__ == '__main__':
    unittest.main()
