import sys


symbolTable = {'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
               'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,
               'R14':14,'R15':15, 'SCREEN':16384, 'KEYBOARD':24576, 'SP':0,
               'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4}
instructions = []
n = 16    #The first availble memory register for varibales
def formatLine(line):
    return line.split('//')[0].strip()

# This function performs the first pass and contruct the symbolTable based on labels of the program
def constructSymbolTable(input_file):
    global symbolTable
    n=-1
    with open(input_file, 'r') as file:
        for line in file:
            if line[0:2] != '//': #comments
                line = formatLine(line)
                if line != '':
                    if line[0] == '(':
                        symbolTable[line[1:len(line)-1]] = n+1
                    else:
                        n+=1


#Functions to tokenize a C-instruction
def dest(instruction):
    if len(instruction) > 2 :
        if instruction[1]=='=' or instruction[2]=='=' or instruction[3]=='=':
            return instruction.split("=")[0]
    return None

def comp(instruction):
    if dest(instruction)!=None:
        return (instruction.split('=')[1]).split(';')[0]
    else:
        return instruction.split(';')[0]

def jmp(instruction):
    if len(instruction.split(';')) > 1:
        return instruction.split(';')[1] if instruction.split(';')[1] != '' else None
    else: 
        return None

#Functions to translate tokens to binary
def destToBinary(token):
    d = {
        None: 0b000,
        'M': 0b001,
        'D': 0b010,
        'MD': 0b011,
        'A': 0b100,
        'AM': 0b101,
        'AD': 0b110,
        'AMD': 0b111
    }
    return format(d[token], '03b')

def compToBinary(token):
    c = {
        '0':0b0101010,
        '1':0b0111111,
        '-1':0b0111010,
        'D':0b0001100,
        'A':0b0110000,
        '!D':0b0001101,
        '!A':0b0110001,
        '-D':0b0001111,
        '-A':0b0110011,
        'D+1':0b0011111,
        'A+1':0b0110111,
        'D-1':0b0001110,
        'A-1':0b0110010,
        'D+A':0b0000010,
        'A+D':0b0000010,
        'D-A':0b0010011,
        'A-D':0b0000111,
        'D&A':0b0000000,
        'D|A':0b0010101,

        'M':0b1110000,
        '!M':0b1110001,
        '-M':0b1110011,
        'M+1':0b1110111,
        'M-1':0b1110010,
        'D+M':0b1000010,
        'M+D':0b1000010,
        'D-M':0b1010011,
        'M-D':0b1000111,
        'D&M':0b1000000,
        'D|M':0b1010101,
    }
    return format(c[token],'07b')

def jmpToBinary(token):
    j = {
        None:0b000,
        'JGT':0b001,
        'JEQ':0b010,
        'JGE':0b011,
        'JLT':0b100,
        'JNE':0b101,
        'JLE':0b110,
        'JMP':0b111
    }
    return format(j[token], '03b')

#Function to concatenate binary codes to get the whole C-instruction translation
def buildCInst(instruction):
    return '111'+compToBinary(comp(instruction))+destToBinary(dest(instruction))+jmpToBinary(jmp(instruction))

#Function to contruct an A-instruction
def buildAInst(symbol):
    global n
    if symbol not in symbolTable.keys() and not symbol.isdigit():
        symbolTable[symbol] = n
        n+=1
    if symbol.isdigit() and int(symbol) < 16:
        return '0' + format(symbolTable['R'+symbol],'015b')
    elif symbol.isdigit() and int(symbol) >= 16:
        return '0' + format(int(symbol),'015b')
    return '0' + format(symbolTable[symbol],'015b')


#Function to perform the second pass in which the translation occurs
def secondPass(input_file):
    instructions.clear()
    with open(input_file, 'r') as file:
        for line in file:
            if line.strip()[0:2] != "//":
                line = formatLine(line)
                if line != '':
                    #check if it is an A-instruction
                    if line[0] == '@':
                        instr = buildAInst(line[1:])
                    elif line[0] == '(':
                        continue
                    #C-instruction
                    else:
                        instr = buildCInst(line)
                    instructions.append(instr)

def main(input_file):
    constructSymbolTable(input_file)
    secondPass(input_file)
    out = input_file.split(".")[0] + "Binary.hack"
    with open(out, 'w') as file:
        for line in instructions:
            file.write(line + '\n')


if __name__ == "__main__":
    input_file = sys.argv[1]
    main(input_file)