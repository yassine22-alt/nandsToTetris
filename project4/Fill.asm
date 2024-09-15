// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
(OLOOP)
    @24576
    D=M
    @WPAINT 
    D;JEQ
    @BPAINT
    0;JMP


 (WPAINT)
    @SCREEN
    D=A
    @addr
    M=D

    @8192
    D=A
    @c
    M=D
    (WCOL)
        @addr
        A=M
        M=0

        @addr
        M=M+1

        @c
        M=M-1
        D=M
        @WCOL
        D;JGT

        @OLOOP
        0;JMP
 

 (BPAINT)
    @SCREEN
    D=A
    @addr
    M=D

    @8192
    D=A
    @r
    M=D
    (BCOL)
        @addr
        A=M
        M=-1

        @addr
        M=M+1

        @r 
        M=M-1
        D=M
        @BCOL
        D;JGT

        @OLOOP
        0;JMP