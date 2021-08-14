from functionB_C import decimal_to_binary
def set_label_addr(instructions):
    label_addr = {} # stores label addr in the format {"label_name1":"binary_addr"}
    for i in range(0, len(instructions)):
        pos_of_colon = instructions[i].find(":")
        if(pos_of_colon!=-1):
            label_addr.update({instructions[i][0:pos_of_colon]:i})
    return label_addr
def set_var_addr(variables, len_instr): #len_instr contains the length of instructions[]
    var_addr = {} # stores variable addr as {"var_name1":"binary_addr1"}
    for i in range(0, len(variables)):
        variables_str=variables[i].split()
        var_addr.update({variables_str[1]:decimal_to_binary(len_instr+i)})
    return var_addr
