# hex_loader.py
import argparse
from emulator.irq_emulator_hook import MockMemory
from emulator.cdp1806e32_emulator import CPU

def load_hex_to_mem(filename, mem, start_addr=0x0100):
    with open(filename) as f:
        addr = start_addr
        for line in f:
            word = int(line.strip(), 16)
            mem.write16(addr, word)
            addr += 2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Run a quick LDI test program")
    parser.add_argument("--hex", type=str, default="monitor.hex", help="Hex file to load")
    args = parser.parse_args()

    mem = MockMemory()

    if args.test:
        print("Running legacy LDI test (F8 42 into R0)...")
        mem.write16(0x0100, 0xFFF8)  # Emulated legacy LDI opcode
        mem.write16(0x0102, 0x0042)  # Value 0x42
        mem.write16(0x0104, 0xE000)  # TRAP to halt
    else:
        print(f"Loading hex file: {args.hex}")
        load_hex_to_mem(args.hex, mem)

    cpu = CPU(mem)
    cpu.pc = 0x0100

    try:
        while True:
            cpu.step()
    except Exception as e:
        print("Program halted:", e)
        print("Registers:", cpu.regs)
