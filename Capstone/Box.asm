
// Nand2Tetris Capstone
// K = 65
// Box: 32 pixels wide, 20 rows tall
// Starting row = 65

(START)
    // Check whether a key is pressed
    @KBD
    D=M
    @SETBLACK
    D;JNE

    // No key: erase the box
    @COLOR
    M=0
    @DRAW
    0;JMP

(SETBLACK)
    // Key pressed: draw black
    @COLOR
    M=-1

(DRAW)
    // Starting address = SCREEN + 32*65
    @SCREEN
    D=A
    @2080
    D=D+A
    @PTR
    M=D

    // Draw 20 rows
    @20
    D=A
    @ROWS
    M=D

(ROWLOOP)
    // Draw 2 words per row (32 pixels)
    @2
    D=A
    @COLS
    M=D

(COLLOOP)
    @COLOR
    D=M
    @PTR
    A=M
    M=D

    // Move to next word
    @PTR
    M=M+1

    @COLS
    M=M-1
    D=M
    @COLLOOP
    D;JGT

    // Skip remaining 30 words to next screen row
    @30
    D=A
    @PTR
    M=D+M

    @ROWS
    M=M-1
    D=M
    @ROWLOOP
    D;JGT

    // Repeat and monitor keyboard
    @START
    0;JMP
