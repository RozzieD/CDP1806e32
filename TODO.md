# CDP1806E-R32: What's Next – Development Roadmap

This document tracks the next recommended tasks and milestones for the CDP1806E-R32 project.

---

## 🔧 GitHub Actions CI
- [ ] Add `.github/workflows/test.yml` (unit test automation)
- [ ] Verify badge in `README.md` renders correctly

## 🧪 Instruction Set Test Coverage
- [ ] Add tests for `CALL` and `RET`
- [ ] Add tests for `PUSH` and `POP`
- [ ] Add tests for `TRAP`
- [ ] Add tests for `LDI imm16`
- [ ] Add memory-mapped I/O read/write test

## 🖥️ Interactive Monitor Shell
- [ ] `monitor.py` with single-step execution
- [ ] Show registers, PC, memory dumps interactively

## 🗃️ Disassembler
- [ ] `disassembler.py` to decode `.hex` back to mnemonics
- [ ] Align output with original source line numbers

## 🔄 Enhanced Assembler
- [ ] Add label support and jump resolving in `asm_to_hex.py`
- [ ] Output intermediate format for debug (`.lst` style)

## 🔌 I/O Emulation
- [ ] Emulate `OUT`/`IN` instructions
- [ ] Hook into `MockMemory` port map (e.g. UART echo)

## 🧵 ROM Monitor Development
- [ ] Write a test monitor program
- [ ] Include serial echo and register display

## 🛠️ FPGA RTL Port
- [ ] Start converting emulator logic into HDL (Verilog or SystemVerilog)
- [ ] Consider LiteX/Migen for SoC scaffolding
- [ ] Plan memory map and instruction decode unit

---

## ⚙️ Optional Long-Term
- [ ] GCC backend port (based on MSP430 or RISC-V)
- [ ] Add advanced Sphinx docs (ISA diagrams, cycle timing)
- [ ] Build interactive debug shell (breakpoints, watchpoints)
