; Minimal Monitor Program (for emulator hex loading)
; Assumes: R9 = Stack Pointer, R10 = Return Address
; Output: Computes 3*7 and traps

        LDI R9, 0xFFFC     ; <-- Set up stack pointer first!
        LDI R1, 3
        LDI R2, 7
        MUL R3, R1, R2
        PUSH R3
        POP R4
        TRAP

; Expected Registers:
;   R3 = 21
;   R4 = 21 (via stack)
;   R9 = SP adjusted and restored
;   Emulator halts with TRAP
