# CDP1806E-R32 Toolchain and Emulator

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/RozzieD/CDP1806e32)](LICENSE)
[![Build Status](https://github.com/RozzieD/cdp1806e32/actions/workflows/test.yml/badge.svg)](https://github.com/RozzieD/cdp1806e32/actions)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://RozzieD.github.io/cdp1806e32/)

A complete open-source softcore CPU system inspired by the RCA COSMAC CDP1802/1806 — reimagined as a 32-bit clean RISC architecture. Designed for embedded RTOS use, FPGA softcore implementation, and real-time Python-based emulation.

---

## 🚀 Features

- ✅ 16 × 32-bit general-purpose registers
- ✅ Clean 16-bit fixed-width instruction set
- ✅ Modular Python-based emulator
- ✅ Push/Pop, arithmetic, conditional branches, and traps
- ✅ Assembler & hex loader for standalone test programs
- ✅ Unit-tested ISA coverage
- 🧪 GCC backend and RISC-V compatibility layer (in development)
- 📘 Sphinx-generated documentation

---

## 🛠️ Getting Started

### Requirements

- Python 3.11+
- `pip` (Python package manager)
- `git`

### Clone & Install

```bash
git clone https://github.com/RozzieD/cdp1806e32
cd cdp1806e32
pip install -r requirements.txt
