from binary_to_decimal import binary_to_decimal
def load(register_file, memory, reg1, mem_addr):
    '''
    Loads data from mem_addr into reg1.

    Input -> reg1 : 3 bit binary string which refers to a register
             mem_addr : 8 bit binary string which refers to memory address
             register_file : List of 16 bit binary strings containing the current state of registers
             memory : List of 16 bit binary strings denoting the memory

    Output -> Returns the updated register file.
    '''
    dict = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    data = memory[binary_to_decimal(mem_addr)]
    register_file[dict[reg1]] = data
    return register_file
def store(register_file, memory, reg1, mem_addr):
    '''
    Stores data from reg1 to mem_addr.

    Input -> reg1 : 3 bit binary string which refers to a register
             mem_addr : 8 bit binary string which refers to memory address
             register_file : List of 16 bit binary strings containing the current state of registers
             memory : List of 16 bit binary strings denoting the memory
    Output -> Returns the updated memory.
    '''
    dict = {'000': 0, '001': 1, '010': 2, '011': 3, '100': 4, '101': 5, '110': 6, '111': 7}
    data = register_file[dict[reg1]]
    memory[binary_to_decimal(mem_addr)] = data
    return memory
