# hex_loader.py

from emulator.irq_emulator_hook import MockMemory

def load_hex_to_mem(filename, mem, start_addr=0x0100):
    with open(filename) as f:
        addr = start_addr
        for line in f:
            word = int(line.strip(), 16)
            mem.write16(addr, word)
            addr += 2

# Example usage:
if __name__ == "__main__":
    from emulator.irq_emulator_hook import MockMemory
    from emulator.cdp1806e32_emulator import CPU

    mem = MockMemory()
    load_hex_to_mem("monitor.hex", mem)

    cpu = CPU(mem)
    cpu.pc = 0x0100

    try:
        while True:
            cpu.step()
    except Exception as e:
        print("Program halted:", e)
        print("Registers:", cpu.regs)
