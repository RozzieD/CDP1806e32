import unittest
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

class TestTrapInstruction(unittest.TestCase):
    def setUp(self):
        self.mem = MockMemory()
        self.cpu = CPU(self.mem)
        self.cpu.pc = 0x0100

    def test_trap_raises_exception(self):
        self.mem.write16(0x0100, 0xE000)  # TRAP
        with self.assertRaises(Exception) as ctx:
            self.cpu.step()
        self.assertIn("TRAP", str(ctx.exception))

if __name__ == '__main__':
    unittest.main()
