# Contributing to CDP1806E-R32

Thanks for considering contributing to the CDP1806E-R32 project!

## How to Contribute

- Fork the repository
- Create a new branch: `git checkout -b feature-name`
- Make your changes with clear commit messages
- Write or update unit tests as appropriate
- Run tests: `python3 -m unittest discover tests`
- Submit a pull request with a summary of your changes

## Code Style

- Follow Python PEP8 conventions for emulator/tests
- Use consistent naming (snake_case in Python, r0–r15 in assembly)
- Keep Verilog/RTL modules modular and documented

## Adding a New Instruction

1. Update the `.md` file for the opcode
2. Extend the emulator logic in `cdp1806e32_emulator.py`
3. Write a test case under `tests/`
4. Document behavior in `api_reference.rst`

## Questions?

Feel free to open an issue on GitHub or contact the maintainer directly.

Happy hacking!