from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal
def add(register_file,reg_code1,reg_code2,reg_code3):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val2=register_file[dict[reg_code2]]
    str_val3=register_file[dict[reg_code3]]
    val2=binary_to_decimal(str_val2)
    val3=binary_to_decimal(str_val3)
    val1=val2+val3
    if(val1>255):
        register_file[7][-4]=1
        return register_file
    str_val1=decimal_to_binary(val1)
    register_file[dict[reg_code1]]='0'*8+str_val1
    return register_file
def sub_func(register_file,reg_code1,reg_code2,reg_code3):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val2=register_file[dict[reg_code2]]
    str_val3=register_file[dict[reg_code3]]
    val2=binary_to_decimal(str_val2)
    val3=binary_to_decimal(str_val3)
    if(val3>val2):
        register_file[dict[reg_code1]]='0'*16
        register_file[7][-4]=1
        return register_file
    val1=val2-val3
    str_val1=decimal_to_binary(val1)
    register_file[dict[reg_code1]]='0'*8+str_val1
    return register_file
def mul_func(register_file,reg_code1,reg_code2,reg_code3):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val2=register_file[dict[reg_code2]]
    str_val3=register_file[dict[reg_code3]]
    val2=binary_to_decimal(str_val2)
    val3=binary_to_decimal(str_val3)
    val1=val2*val3
    if(val1>255):
        register_file[7][-4]=1
        return register_file
    str_val1=decimal_to_binary(val1)
    register_file[dict[reg_code1]]='0'*8+str_val1
    return register_file
def div_func(register_file,reg_code3,reg_code4):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val1=register_file[dict[reg_code3]]
    str_val2=register_file[dict[reg_code4]]
    val3=binary_to_decimal(str_val1)
    val4=binary_to_decimal(str_val2)
    quotient=val3/val4
    remeinder=val3%val4
    str_quo=decimal_to_binary(quotient)
    str_quo+='0'*8+str_quo
    str_rem=decimal_to_binary(remeinder)
    str_rem+='0'*8+str_rem
    register_file[0]=str_quo
    register_file[1]=str_rem
    return register_file
