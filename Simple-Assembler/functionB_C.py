import error

def decimal_to_binary(num,line_no):
    '''
    returns string containing 8 bit binary conversion of num
    num -> integer
    '''
    if(int(num)<0 or int(num)>255):
        raise error.ImmediateException("Illegal immediate values",line_no)
    binary = [0, 0, 0, 0, 0, 0, 0, 0]
    dividend = int(num)
    quotient = -1
    k = 7
    while (quotient != 0 and k >= 0):
        quotient = dividend // 2
        binary[k] = dividend % 2
        k = k - 1
        dividend = quotient
    return "".join(map(str, binary))
def typeB(opcode, reg1, imm):
    '''
    returns the encoding of type B instructions
    opcode -> string
    reg1 -> string
    imm -> string
    '''
    return opcode + reg1 + imm
def typeC(opcode, reg1, reg2):
    '''
    returns the encoding of type C instructions
    opcode -> string
    reg1 -> string
    reg2 -> string
    '''
    return opcode + "00000" + reg1 + reg2
def func_B_C(instruction,line_no):
    '''
    returns the string encoding of instruction on the basis of whether it is type B or C
    instruction -> list
    '''
    instruction=instruction.split()
    if(len(instruction)!=3):
        raise error.SyntaxException("Illegal use of syntax",line_no)
    reg_address = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
                   "R4": "100", "R5": "101", "R6": "110","FLAGS":"111"}
    x=instruction[1]
    if(x not in reg_address):
        raise error.SyntaxException("Invalid use of registers",line_no)
    if (instruction[0] == "mov" and instruction[2][0] == "$"):  # type B
        opcode = "00010"
        encoding = typeB(opcode, reg_address[instruction[1]], decimal_to_binary(instruction[2][1:],line_no))
    elif (instruction[0] == "mov" and instruction[2][0] != "$"):  # type C
        opcode = "00011"
        if(instruction[2] not in reg_address):
            raise error.SyntaxException("Invalid use of registers",line_no)
        encoding = typeC(opcode, reg_address[instruction[1]], reg_address[instruction[2]])
    elif (instruction[0] == "div"):  # type C
        opcode = "00111"
        if (instruction[2] not in reg_address):
            raise error.SyntaxException("Invalid use of registers",line_no)
        if(instruction[2]=="FLAGS"):
            raise error.FlagException("Invlaid use of FLAGS",line_no)
        encoding = typeC(opcode, reg_address[instruction[1]], reg_address[instruction[2]])
    elif (instruction[0] == "rs"):  # type B
        opcode = "01000"
        encoding = typeB(opcode, reg_address[instruction[1]], instruction[2])
    elif (instruction[0] == "ls"):  # type B
        opcode = "01001"
        encoding = typeB(opcode, reg_address[instruction[1]], instruction[2])
    elif (instruction[0] == "not"):  # type C
        opcode = "01101"
        if (instruction[2] not in reg_address):
            raise error.SyntaxException("Invalid use of registers",line_no)
        if(instruction[2]=="FLAGS"):
            raise error.FlagException("Invalid use of FLAGS",line_no)
        encoding = typeC(opcode, reg_address[instruction[1]], reg_address[instruction[2]])
    elif (instruction[0] == "cmp"):  # type C
        opcode = "01110"
        if (instruction[2] not in reg_address):
            raise error.SyntaxException("Invalid use of registers",line_no)
        if (instruction[2]=="FLAGS"):
            raise error.FlagException("Invalid use of FLAGS",line_no)
        encoding = typeC(opcode, reg_address[instruction[1]], reg_address[instruction[2]])
    return encoding
