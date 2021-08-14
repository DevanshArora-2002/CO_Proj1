import error 
import decimal_to_binary from functionB_C
def func_D(user_input,dict_input):
    arr=user_input.split() # storing user input in array
    if(len(arr)!=3):
        raise error.SyntaxException("Illegal use of syntax")
    if(arr[0]=="ld"):
        opcode="00100"
    if(arr[0]=="st"):
        opcode="00101"
    reg_address = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
                   "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
    if(arr[1] not in reg_address):
        raise error.SyntaxException("Invalid use if registers")
    if(arr[2] not in dict_input):
        raise error.IllegalVariable("Variable declaration missing")
    x=dict_input[arr[2]] # getting numeric value from input dictionary
    y=decimal_to_binary(x) # converting decimal to binary
    return opcode+reg_address[arr[1]]+y
def func_E(user_input,dict_input):
    arr=user_input.split()
    if(arr[1] not in dict_input):
        raise error.IllegalLabel("Label declaration missing")
    if(len(arr)!=2):
        raise error.SyntaxException("Illegal use of syntax")
    if(arr[0]=="jmp"):
        opcode="01111"
    if(arr[0]=="jlt"):
        opcode="10000"
    if(arr[0]=="jgt"):
        opcode="10001"
    if(arr[0]=="je"):
        opcode="10010"
    x=dict_input[arr[1]] # getting numeric value from input dictionary
    y=decimal_to_binary(x) # converting decimal to binary
    return opcode+"000"+y # "000" for unused binary bits 
  
