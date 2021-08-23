from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal
def uncond_jump(mem_addr):
    return program_counter
def lt_jump(register_file,program_counter,mem_addr):
    flag_reg=register_file[-1]
    if(flag_reg[-3]==1):
        program_counter=binary_to_decimal(mem_addr)
        register_file[-1][-3]=0
    return register_file,program_counter
def gt_jump(register_file,program_counter,mem_addr):
    flag_reg=register_file[-1]
    if(flag_reg[-2]==1):
        program_counter=binary_to_decimal(mem_addr)
        register_file[-1][-2]=0
    return register_file,program_counter
def eq_jump(register_file,program_counter,mem_addr):
    flag_reg=register_file[-1]
    if(flag_reg[-1]==1):
        program_counter=binary_to_decimal(mem_addr)
        register_file[-1][-1]=0
    return register_file,program_counter
