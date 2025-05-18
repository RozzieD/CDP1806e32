# CDP1806E-R32 Toolchain and Emulator

[![Build Status](https://github.com/RozzieD/cdp1806e32/actions/workflows/test.yml/badge.svg)](https://github.com/RozzieD/cdp1806e32/actions)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://RozzieD.github.io/cdp1806e32/)

A complete open-source softcore CPU system inspired by the COSMAC 1802 and modernized into a clean 32-bit RISC architecture. Designed for embedded RTOS, FPGA softcore, and real-time emulation.

## Features
- 16×32-bit general-purpose registers
- 16-bit RISC-like instructions
- GCC backend (in development)
- Python-based emulator with disassembler
- Memory-mapped I/O and IRQ support
- UART, Timer, and syscall interfaces
- GitHub Actions CI + Sphinx Docs

## Getting Started

```bash
git clone https://github.com/RozzieD/cdp1806e32
cd cdp1806e32
make
python3 cdp1806e32_emulator.py
```

To run tests:
```bash
python3 -m unittest discover tests
```

To build documentation:
```bash
sphinx-build -b html docs/ docs/_build
```

---

## License
MIT

---

## Contributing
Pull requests are welcome! Please include tests for new features and follow the existing code style.

---

## Authors
Maintained by RozzieD.
