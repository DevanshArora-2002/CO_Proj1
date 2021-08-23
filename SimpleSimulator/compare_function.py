from binary_to_decimal import binary_to_decimal
from decimal_to_binary import decimal_to_binary
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
        register_file[-1]='0'*12+'0010'
        return register_file
    if(val1<val2):
        register_file[-1]='0'*12+'0100'
        return register_file
    else:
        register_file[-1]='0'*12+'0001'
        return register_file
