from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal
def uncond_jump(register_file,mem_addr):
    program_counter=binary_to_decimal(mem_addr)
    return register_file,program_counter
def lt_jump(register_file,program_counter,mem_addr):
    flag_reg=register_file[-1]
    if(flag_reg[-3]=='1'):
        program_counter=binary_to_decimal(mem_addr)
        str1=register_file[-1][0:-3]
        str2=register_file[-1][-2:]
        register_file=str1+'0'+str2
    else:
        program_counter+=1
    return register_file,program_counter
def gt_jump(register_file,program_counter,mem_addr):
    flag_reg=register_file[-1]
    if(flag_reg[-2]=='1'):
        program_counter=binary_to_decimal(mem_addr)
        str1=register_file[-1][0:-2]
        str2=register_file[-1][-1]
        register_file[-1]=str1+'0'+str2
    else:
        program_counter+=1
    return register_file,program_counter
def eq_jump(register_file,program_counter,mem_addr):
    flag_reg=register_file[-1]
    if(flag_reg[-1]=='1'):
        program_counter=binary_to_decimal(mem_addr)
        str1=register_file[-1][0:-1]
        register_file[-1]=str1+'0'
    else:
        program_counter+=1
    return register_file,program_counter