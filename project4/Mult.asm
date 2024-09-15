// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.

// Result Varibale
@p 
M=0

// If RAM[0] = 0: goto EXIT
@R0
D=M;
@EXIT
D;JEQ
// If RAM[1] = 0: goto EXIT
@R1
D=M;
@EXIT
D;JEQ

(DEB)
    @R0
    D=M;
    // n = RAM[0]
    @n
    M=D;
    // if n < 0: goto NEG
    @NEG
    D;JLT
    

(LOOP)
    // D = RAM[1]
    @R1
    D=M
    // p += RAM[1]
    @p
    M=M+D
    // n -= 1
    @n 
    MD=M-1
    // if n==0: goto EXIT
    @EXIT
    D;JEQ
    
    @LOOP
    0;JMP


// n *= -1
(NEG)
    @n
    M=-D;
    @LOOP
    0;JMP

(EXIT)
    // RAM[2] = p
    @p
    D=M 
    @R2
    M=D
    // if RAM[0] < 0 : goto RNEG
    @R0
    D=M 
    @RNEG
    D;JLT




(FIN)
    @FIN
    0;JMP

(RNEG)
    // RAM[2] *= -1
    @R2
    M=-M;
    @FIN
    0;JMP