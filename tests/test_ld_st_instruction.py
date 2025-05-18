import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestLdStInstructions(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_ld_and_st(self):
        # Store test: R1 = 0xABCD1234, address = R2 + 0x1 = 0x2001
        self.cpu.regs[1] = 0xABCD1234
        self.cpu.regs[2] = 0x2000

        # ST R1 -> [R2 + 1] => opcode=8, rd=1, rs=2, rt=1 => 1000 0001 0010 0001 = 0x8121
        self.mem.write16(0x0100, 0x8121)
        self.cpu.step()

        val_written = self.mem.read32(0x2001)
        self.assertEqual(val_written, 0xABCD1234)

        # Now test LD: clear R3 first
        self.cpu.regs[3] = 0

        # LD R3 <- [R2 + 1] => opcode=7, rd=3, rs=2, rt=1 => 0111 0011 0010 0001 = 0x7321
        self.mem.write16(0x0102, 0x7321)
        self.cpu.step()

        self.assertEqual(self.cpu.regs[3], 0xABCD1234)

if __name__ == '__main__':
    unittest.main()
