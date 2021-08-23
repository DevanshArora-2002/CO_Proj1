from decimal_to_binary import decimal_to_binary
from binary_to_decimal import binary_to_decimal
class program_counter():
    def __init__(self,counter_value):
        """
        The value of PC is saved in Integer format
        :param counter_value:
        """
        self.pc=counter_value
    def getval(self):
        """
        This returns PC in integer value format
        :return:
        """
        return self.pc
    def dump(self):
        """
        Returns the value in binary coded format
        :return:
        """
        val=decimal_to_binary(self.pc)
        print(val,end=" ")
    def update(self,counter_value):
        """
        Updates the value of PC
        :param counter_value:
        :return:
        """
        self.pc=counter_value
        pass
    pass
