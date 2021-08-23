class RegisterRecord():
    """
    This class saves the register file as it's own register_file
    Initially the value of all registers are set to 0 in string format
    """
    def __init__(self):
        str1='0'*16
        self.register_file=[]
        for i in range(0,8):
            self.register_file.append(str1)
    pass
    def dump(self):
        for i in range(0,8):
            print(self.register_file[i],end=" ")
        print()
pass
