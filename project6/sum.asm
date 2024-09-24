@R0
D=M
@n		//n = RAM[0]	
M=D

@i
M=1		//i = 1

@sum
M=0		//sum = 0

(LOOP)
@i
D=M
@n
D=D-M
@STOP		//if i>n :goto STOP
D;JGT

@i
D=M
@sum
M=M+D		//sum +=i
@i
M=M+1		//i +=1
@LOOP
0;JMP		//goto LOOP

(STOP)
@sum
D=M
@R1		//RAM[1]=sum
M=D

(EXIT)
@EXIT
0;JMP