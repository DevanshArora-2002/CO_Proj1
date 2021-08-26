from binary_to_decimal import binary_to_decimal
from decimal_to_binary import decimal_to_binary
def ls_func(register_file,reg_code1,imm):
    dict = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    str_val1=register_file[dict[reg_code1]]
    val1=binary_to_decimal(str_val1)
    imm1=binary_to_decimal(imm)
    val=val1>>imm1
    val=decimal_to_binary(val)
    register_file[dict[reg_code1]]='0'*8+str(val)
    return register_file
def rs_func(register_file,reg_code1,imm):
    dict = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    str_val1=register_file[dict[reg_code1]]
    val1=binary_to_decimal(str_val1)
    imm1=binary_to_decimal(imm)
    val=val1<<imm1
    val=decimal_to_binary(val)
    register_file[dict[reg_code1]]='0'*8+str(val)
    return register_file
