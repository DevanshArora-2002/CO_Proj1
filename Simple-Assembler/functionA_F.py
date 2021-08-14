import error
def func_A(user_input):
    arr=user_input.split()
    if(len(arr)!=4):
        raise error.SyntaxException("Illegal use of syntax")
    x=arr[1]
    y=arr[2]
    z=arr[3]
    reg_address = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
                   "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
    if (x not in reg_address or y not in reg_address or z not in reg_address):
        raise error.SyntaxException("Invalid Use of Registers")
    if(arr[0]=="add"):
        opcode="00000"
    if(arr[0]=="sub"):
        opcode="00001"
    if(arr[0]=="mul"):
        opcode="00110"
    if(arr[0]=="xor"):
        opcode="01010"
    if(arr[0]=="or"):
        opcode="01011"
    if(arr[0]=="and"):
        opcode="01100"
    return opcode+"00"+reg_address[x]+reg_address[y]+reg_address[z]
def func_F():
    return "10011"+"00000000000"
