def binary_to_decimal(str):
    num=0
    for i in range(1,9):
        num+=int(str[-i])*2**(i-1)
    return num
def decimal_to_binary(num):
    binary = [0,0,0,0,0,0,0,0]
    dividend = int(num)
    quotient = -1
    k=7
    while(quotient!=0 and k>=0):
        quotient = dividend//2
        binary[k] = dividend%2
        k=k-1
        dividend = quotient
    return "".join(map(str, binary))
def cmp(register_file,reg_code1,reg_code2):
    dict = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    str_val1 = register_file[dict[reg_code1]]
    str_val2 = register_file[dict[reg_code2]]
    val1=binary_to_decimal(str_val1)
    val2=binary_to_decimal(str_val2)
    """
    This function is used to compare reg_code1 with that of reg_code2
    and then sets the flag register accordingly
    """
    if(val1>val2):
        register_file[-1][-2]=1
        return register_file
    if(val1<val2):
        register_file[-1][-3]=1
        return register_file
    else:
        register_file[-1][-1]=1
        return register_file
