from binary_to_decimal import binary_to_decimal
#from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal


class Memory:
    def _init_(self):
        '''
        Initializes memory to an array of length 256 with 16 bit 0s in string format.
        '''
        self.self = ["0000000000000000"] * 256

    def initialize(self, instructions):
        '''
        Copies instructions to memory in appropriate locations.
        Input -> instructions : list of 16 bit binary strings
        '''
        for i in range(len(instructions)):
            self.self[i] = instructions[i]

    def set_value_using_PC(self, value, PC):
        '''
        Sets the value of a particular location pointed by PC in memory.
        Input -> value : 8 bit binary string
                 PC : 8 bit binary string
        '''
        self.self[binary_to_decimal(PC) - 1] = "00000000" + value

    def fetch_using_PC(self, PC):
        '''
        Returns the value stored a location pointed by PC.
        Input -> PC : 8 bit binary string
        Output -> 16 bit binary string
        '''
        return self.self[binary_to_decimal(PC) - 1]

    def dump(self):
        '''
        Prints the entire contents of the memory.
        '''
        for i in range(len(self.self)):
            print(self.self[i])
