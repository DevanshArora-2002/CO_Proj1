from op_functions import sub_func,mul_func,div_func,add_func
from bit_func import xor_func,or_func,and_func,not_func
from shift_func import ls_func,rs_func
from mov_func import mov_reg,mov_imm
from jumping import gt_jump,lt_jump,eq_jump,uncond_jump
from compare_function import cmp
from load_store import load,store
class ExecutionEngine():
    def __init__(self,memory,program_counter):
        self.memory=memory
        self.program_counter=program_counter
        self.compare=False
        self.overflow=False
        """if the next instruction to compare instruction 
           is not a jump instruction then the flag is set to 0
        """
        pass
    def execute(self,instr,PC,reg_file,cycle):
        mem_lst = []
        opcode=instr[0:5]
        if(opcode in ['00000','00001','00110','00111']):
            if(self.overflow):
                register=reg_file.register_file
                register[-1]='0'*16
                reg_file.update(register)
                self.overflow=False
            """
            The code for arthemetic operations
            """
            reg_code3 = instr[-3:]
            """
            For div function reg_code3 will act as the reg_code2 and similarly for 
            reg_code1 and reg_code2
            """
            reg_code2 = instr[-6:-3]
            reg_code1 = instr[-9:-6]
            if(opcode!='00111'):                
                if(opcode=='00000'):                    
                    updated_reg_file,self.overflow=add_func(reg_file.register_file,reg_code1,reg_code2,reg_code3)
                    reg_file.update(updated_reg_file)         
                elif(opcode=='00001'):
                    updated_reg_file,self.overflow=sub_func(reg_file.register_file,reg_code1,reg_code2,reg_code3)
                    reg_file.update(updated_reg_file)
                else:
                    updated_reg_file,self.overflow=mul_func(reg_file.register_file,reg_code1,reg_code2,reg_code3)
                    reg_file.update(updated_reg_file)
            else:
                updated_reg_file=div_func(reg_file.register_file,reg_code2,reg_code3)
                reg_file.update(updated_reg_file)
            PC+=1
            if(self.compare):
                register=reg_file.register_file
                register[-1]='0'*16
                reg_file.update(register)
                self.compare=False       
            return False,PC,reg_file,mem_lst
        elif(opcode in ['01000','01001']):
            """
            This code is for shift operations
            """
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
            imm=instr[-8:]
            reg_code=instr[5:8]
            if(opcode=='01000'):
                updated_reg_file=rs_func(reg_file.register_file,reg_code,imm)
                reg_file.update(updated_reg_file)
            else:
                updated_reg_file=ls_func(reg_file.register_file,reg_code,imm)
                reg_file.update(updated_reg_file)
            PC+=1
            if(self.compare):
                register=reg_file.register_file
                register[-1]='0'*16
                reg_file.update(register)
                self.compare=False
            return False, PC,reg_file,mem_lst
        elif(opcode in ['01010','01011','01100','01101']):
            """
            This code is for bitwise operations
            """
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
            reg_code3 = instr[-3:]
            """
            For div function reg_code3 will act as the reg_code2 and similarly for 
            reg_code1 and reg_code2
            """
            reg_code2 = instr[-6:-3]
            reg_code1 = instr[-9:-6]
            if(opcode!='01101'):
                if(opcode=='01010'):
                    updated_reg_file=xor_func(reg_file.register_file,reg_code1,reg_code2,reg_code3)
                    reg_file.update(updated_reg_file)
                elif(opcode=='01011'):
                    updated_reg_file=or_func(reg_file.register_file,reg_code1,reg_code2,reg_code3)
                    reg_file.update(updated_reg_file)
                else:
                    updated_reg_file=and_func(reg_file.register_file,reg_code1,reg_code2,reg_code3)
                    reg_file.update(updated_reg_file)
            else:
                updated_reg_file=not_func(reg_file.register_file,reg_code2,reg_code3)
                reg_file.update(updated_reg_file)
            PC+=1
            if(self.compare):
                register=reg_file.register_file
                register[-1]='0'*16
                reg_file.update(register)
                self.compare=False       
            return False, PC,reg_file,mem_lst
        elif(opcode in ['00010','00011']):
            """
            This is for mov instruction
            """
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
            if(opcode=='00011'):
                reg_code2=instr[-3:]
                reg_code1=instr[-6:-3]
                updated_reg_file=mov_reg(reg_file.register_file,reg_code1,reg_code2)
                reg_file.update(updated_reg_file)
            else:
                imm=instr[-8:]
                reg_code=instr[5:8]
                updated_reg_file=mov_imm(reg_file.register_file,reg_code,imm)
                reg_file.update(updated_reg_file)
            PC+=1
            if(self.compare):
                register=reg_file.register_file
                register[-1]='0'*16
                reg_file.update(register)
                self.compare=False       
            return False, PC,reg_file, mem_lst
        elif(opcode=='01110'):
            """
            This code is for compare instructions
            """
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
            reg_2=instr[-3:]
            reg_1=instr[-6:-3]
            updated_reg_file=cmp(reg_file.register_file,reg_1,reg_2)
            reg_file.update(updated_reg_file)
            PC+=1
            self.compare=True
            return False,PC,reg_file,mem_lst
        elif(opcode in ['01111','10000','10001','10010']):
            """
            This code is for jump instructions
            """
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
            mem_addr=instr[-8:]
            mem_lst.append(mem_addr)
            if(opcode=='01111'):
                updated_reg_file,nextPC=uncond_jump(reg_file.register_file,mem_addr)
                reg_file.update(updated_reg_file)
                if (self.compare):
                    register = reg_file.register_file
                    register[-1] = '0' * 16
                    reg_file.update(register)
                    self.compare = False
                return False,nextPC,reg_file,mem_lst
            elif(opcode=='10000'):
                updated_reg_file,nextPC=lt_jump(reg_file.register_file,PC,mem_addr)
                reg_file.update(updated_reg_file)
                if (self.compare):
                    register = reg_file.register_file
                    register[-1] = '0' * 16
                    reg_file.update(register)
                    self.compare = False
                return False,nextPC,reg_file,mem_lst
            elif(opcode=='10001'):
                updated_reg_file,nextPC=gt_jump(reg_file.register_file,PC,mem_addr)
                reg_file.update(updated_reg_file)
                if (self.compare):
                    register = reg_file.register_file
                    register[-1] = '0' * 16
                    reg_file.update(register)
                    self.compare = False
                return False,nextPC,reg_file,mem_lst
            elif(opcode=='10010'):
                updated_reg_file,nextPC=eq_jump(reg_file.register_file,PC,mem_addr)
                reg_file.update(updated_reg_file)
                if (self.compare):
                    register = reg_file.register_file
                    register[-1] = '0' * 16
                    reg_file.update(register)
                    self.compare = False
                return False,nextPC,reg_file,mem_lst
            
        elif(opcode in ['00101','00100']):
            """
            This is the code for load store instructions
            """
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
            mem_addr = instr[-8:]
            mem_lst.append(mem_addr)
            if(opcode=='00100'):
                updated_reg_file=load(reg_file.register_file,self.memory,instr[5:8],mem_addr)
                reg_file.update(updated_reg_file)
                PC+=1
                return False,PC,reg_file,mem_lst
            else:
                self.memory=store(reg_file.register_file,self.memory,instr[5:8],mem_addr)
                PC+=1
                if(self.compare):
                    register=reg_file.register_file
                    register[-1]='0'*16
                    reg_file.update(register)
                    self.compare=False       
                return False,PC,reg_file,mem_lst
        else:
            if (self.overflow):
                register = reg_file.register_file
                register[-1] = '0' * 16
                reg_file.update(register)
                self.overflow = False
                if (self.compare):
                    register = reg_file.register_file
                    register[-1] = '0' * 16
                    reg_file.update(register)
                    self.compare = False
            return True,PC,reg_file,mem_lst
