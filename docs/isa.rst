CDP1806 vs CDP1806E-R32 Opcode Map (Extended)
=============================================

.. list-table:: Instruction Set Comparison
   :widths: 15 20 20 30
   :header-rows: 1

   * - Functional Group
     - CDP1806 Mnemonic & Opcode (Hex)
     - CDP1806E-R32 Mnemonic & Encoding
     - Notes

   * - Load Immediate
     - LDI (F8)
     - LDI rd, imm16 → 0x93R + 16-bit immediate
     - Load 16-bit constant into register

   * - Register Move
     - 
     - MOV rd, rs → 0x3RS0
     - Copy register (RISC-style)

   * - Get/Put Byte
     - GHI Rn / PLO Rn (9n / An)
     - N/A
     - Replaced by full 32-bit registers

   * - Arithmetic: ADD
     - INC Rn (1n)
     - ADD rd, rs, rt → 0x1RST
     - Replaces INC/DEC with 3-op ADD

   * - Arithmetic: SUB
     - DEC Rn (2n)
     - SUB rd, rs, rt → 0x2RST
     - Full subtraction

   * - Arithmetic: ADDI
     - ADI (C1)
     - ADDI rd, imm → 0x91RI
     - Immediate addition

   * - Arithmetic: SUBI
     - SDI (C2)
     - SUBI rd, imm → 0x92RI
     - Immediate subtraction

   * - Logic: AND
     - AND (C4)
     - AND rd, rs, rt → 0x4RST
     - Logical AND

   * - Logic: OR
     - OR (C5)
     - OR rd, rs, rt → 0x5RST
     - Logical OR

   * - Logic: XOR
     - XOR (C6)
     - XOR rd, rs, rt → 0x6RST
     - Logical XOR

   * - Logic: NOT / NEG
     - 
     - NEG rd → 0xB000 | NOT rd → 0xB010
     - Unary logic operations

   * - Shift/Rotate
     - SHL / SHR / ROL / ROR
     - SHL rd → 0xC010 | SHR rd → 0xC011
     - Shift/rotate operations

   * - Memory: Load
     - LDR Rn (6n)
     - LD rd, [rs+imm4] → 0x7RST
     - Register indirect load

   * - Memory: Store
     - STR Rn (7n)
     - ST [rs+imm4], rd → 0x8RST
     - Register indirect store

   * - Branch
     - BR, BZ, BNZ, BDF, BNF, BQ, BNQ
     - BEQ, BNE, BGT, BLT, BGE, BLE → 0xD0CC
     - Expanded conditional branches

   * - Compare
     - 
     - CMP rd, rs → 0xDRS0
     - Sets condition flags

   * - Stack Ops
     - 
     - PUSH Rn → 0xB0Rn | POP Rn → 0xB1Rn
     - Stack manipulation via SP (R9)

   * - Call/Return
     - SCAL, SEP Rn / SRET
     - CALL → 0xC000 (Jumps to R10, pushes PC), RET → 0xF000 (Pops PC)
     - Call and return

   * - Trap/Break
     - DIS, IDLE
     - TRAP → 0xE000
     - System halt or software interrupt

   * - Control: CSR Access
     - 
     - CSRR rd, csr → 0xE1RC | CSRW csr, rs → 0xE2RC
     - Read/write system registers

   * - I/O: Output
     - OUT n (3n)
     - OUT port, reg → 0xE3RP
     - MMIO output

   * - I/O: Input
     - INP n (4n)
     - IN reg, port → 0xE4RP
     - MMIO input

   * - Skip Instructions
     - SKP / LSK / LSN
     - N/A
     - May be implemented with conditional branches

   * - NOP
     - NOP (00)
     - NOP → 0x0000
     - No operation

   * - Multiply / Divide
     - 
     - MUL rd, rs, rt → 0xA??? | DIV → 0xB2RST
     - Optional extended ALU

   * - Memory Extended
     - 
     - LDI rd, imm16 → 0x93RR + 16-bit ext
     - Extended load with prefix
