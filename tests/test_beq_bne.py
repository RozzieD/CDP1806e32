import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestBranchInstructions(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_beq_taken(self):
        # Set Z flag
        self.cpu.flag_z = 1
        # BEQ +2: opcode=0xC, cond=0x0 (EQ), offset=0x02 => 1100 0000 0000 0010 = 0xC002
        self.mem.write16(0x0100, 0xC002)
        self.cpu.step()
        self.assertEqual(self.cpu.pc, 0x0104)

    def test_beq_not_taken(self):
        self.cpu.flag_z = 0
        self.mem.write16(0x0100, 0xC002)  # BEQ +2
        self.cpu.step()
        self.assertEqual(self.cpu.pc, 0x0102)

    def test_bne_taken(self):
        self.cpu.flag_z = 0
        self.mem.write16(0x0100, 0xC102)  # BNE +2
        self.cpu.step()
        self.assertEqual(self.cpu.pc, 0x0104)

    def test_bne_not_taken(self):
        self.cpu.flag_z = 1
        self.mem.write16(0x0100, 0xC102)  # BNE +2
        self.cpu.step()
        self.assertEqual(self.cpu.pc, 0x0102)

if __name__ == '__main__':
    unittest.main()
# This test suite tests the BEQ and BNE instructions of the CPU.
# It checks the program counter after executing these instructions based on the zero flag.