from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal
def xor_func(register_file,reg_code1,reg_code2,reg_code3):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val2=register_file[dict[reg_code2]]
    str_val3=register_file[dict[reg_code3]]
    val2=decimal_to_binary(str_val2)
    val3=decimal_to_binary(str_val3)
    val4=val2^val3
    register_file[dict[reg_code1]]='0'*8+str(val4)
    return register_file
def or_func(register_file,reg_code1,reg_code2,reg_code3):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val2=register_file[dict[reg_code2]]
    str_val3=register_file[dict[reg_code3]]
    val2=decimal_to_binary(str_val2)
    val3=decimal_to_binary(str_val3)
    val4=val2|val3
    register_file[dict[reg_code1]]='0'*8+str(val4)
    return register_file
def and_func(register_file,reg_code1,reg_code2,reg_code3):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val1=register_file[dict[reg_code1]]
    str_val2=register_file[dict[reg_code2]]
    val1=decimal_to_binary(str_val1)
    val2=decimal_to_binary(str_val2)
    val3=val1&val2
    register_file[dict[reg_code1]]='0'*8+str(val3)
    return register_file
def not_func(register_file,reg_code1,reg_code2):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    str_val1=register_file[dict[reg_code1]]
    str_val2=register_file[dict[reg_code2]]
    val1=decimal_to_binary(str_val1)
    val2=decimal_to_binary(str_val2)
    val3=~val2
    register_file[dict[reg_code1]]='0'*8+str(val3)
    return register_file
