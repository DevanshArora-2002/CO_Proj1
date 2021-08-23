def mov_reg(register_file,reg_code1,reg_code2):
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    register_file[dict[reg_code1]]=register_file[dict[reg_code2]]
    return register_file
def mov_imm(register_file,reg_code1,imm):
    val=imm
    dict={'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
    register_file[dict[reg_code1]]='0'*8+val
    return register_file
