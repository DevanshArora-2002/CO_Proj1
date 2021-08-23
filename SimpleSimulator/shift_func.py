def ls_func(register_file,reg_code1,imm):
    str_val1=register_file[dict[reg_code1]]
    val1=binary_to_decimal(str_val1)
    imm1=binary_to_decimal(imm)
    val=val1<<imm1
    register_file[dict[reg_code1]]='0'*8+str(val)
    return register_file
def rs_func(register_file,reg_code1,imm):
    str_val1=register_file[dict[reg_code1]]
    val1=binary_to_decimal(str_val1)
    imm1=binary_to_decimal(imm)
    val=val1>>imm1
    register_file[dict[reg_code1]]='0'*8+str(val)
    return register_file
