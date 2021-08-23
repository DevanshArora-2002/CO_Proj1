from op_functions import sub_func,mul_func,div_func,add_func
from bit_func import xor_func,or_func,and_func,not_func
from shift_func import ls_func,rs_func
from mov_func import mov_reg,mov_imm
from jumping import gt_jump,lt_jump,eq_jump,uncond_jump
from op_functions import binary_to_decimal,decimal_to_binary
from compare_function import cmp
from load_store import load,store
class ExecutionEngine():
    def __init__(self,memory,register_file,program_counter):
        self.reg_file=register_file
        self.memory=memory
        self.program_counter=program_counter
        pass
    def execute(self,instr,cycle):
        opcode=instr[0:5]
        if(opcode in ['00000','00001','00110','00111']):
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
                    self.reg_file=add_func(self.reg_file,reg_code1,reg_code2,reg_code3)
                elif(opcode=='00001'):
                    self.reg_file=sub_func(self.reg_file,reg_code1,reg_code2,reg_code3)
                else:
                    self.reg_file=mul_func(self.reg_file,reg_code1,reg_code2,reg_code3)
            else:
                self.reg_file=div_func(self.reg_file,reg_code2,reg_code3)
            val=binary_to_decimal(self.program_counter)
            val+=1
            self.program_counter.update(val)
            return False,self.program_counter
        elif(opcode in ['01000','01001']):
            """
            This code is for shift operations
            """
            imm=instr[-8:]
            reg_code=instr[-11:-8]
            if(opcode=='01000'):
                self.reg_file=rs_func(self.reg_file,reg_code,imm)
            else:
                self.reg_file=ls_func(self.reg_file,reg_code,imm)
            val = binary_to_decimal(self.program_counter.dump())
            val += 1
            self.program_counter.update(val)
            return False, self.program_counter
        elif(opcode in ['01010','01011','01100','01101']):
            """
            This code is for bitwise operations
            """
            reg_code3 = instr[-3:]
            """
            For div function reg_code3 will act as the reg_code2 and similarly for 
            reg_code1 and reg_code2
            """
            reg_code2 = instr[-6:-3]
            reg_code1 = instr[-9:-6]
            if(opcode!='01101'):
                if(opcode=='01010'):
                    self.reg_file=xor_func(self.reg_file,reg_code1,reg_code2,reg_code3)
                elif(opcode=='01011'):
                    self.reg_file=or_func(self.reg_file,reg_code1,reg_code2,reg_code3)
                else:
                    self.reg_file=and_func(self.reg_file,reg_code1,reg_code2,reg_code3)
            else:
                self.reg_file=not_func(self.reg_file,reg_code2,reg_code3)
            val = binary_to_decimal(self.program_counter.dump())
            val += 1
            self.program_counter.update(val)
            return False, self.program_counter
        elif(opcode in ['00010','00011']):
            """
            This is for mov instruction
            """
            if(opcode=='00010'):
                reg_code2=instr[-3:]
                reg_code1=instr[-6:-3]
                self.reg_file=mov_reg(self.reg_file,reg_code1,reg_code2)
            else:
                imm=instr[-8:]
                reg_code=instr[-11:-8]
                self.reg_file=mov_imm(self.reg_file,reg_code,imm)
            val = binary_to_decimal(self.program_counter.dump())
            val += 1
            self.program_counter.update(val)
            return False, self.program_counter
        elif(opcode=='01110'):
            """
            This code is for compare instructions
            """
            reg_2=instr[-3:]
            reg_1=instr[-6:-3]
            self.reg_file=cmp(self.reg_file,reg_1,reg_2)
            val=binary_to_decimal(self.program_counter.dump())
            val+=1
            self.program_counter.update(val)
            return False,self.program_counter
        elif(opcode in ['01111','10000','10001','10010']):
            """
            This code is for jump instructions
            """
            flag = self.reg_file[7]
            if(opcode=='01111'):
                self.program_counter.update(binary_to_decimal(instr[-8:]))
                return False,self.program_counter
            elif(opcode=='10000'):
                if(flag[-3]==1):
                    self.reg_file[7][-3]=0
                    self.program_counter.update(binary_to_decimal(instr[-8:]))
                    return False,self.program_counter
            elif(opcode=='10001'):
                if(flag[-2]==1):
                    self.reg_file[7][-2]=0
                    self.program_counter.update(binary_to_decimal(instr[-8:]))
                    return False,self.program_counter
            elif(opcode=='10010'):
                if(flag[-1]==1):
                    self.reg_file[7][-1]=0
                    self.program_counter.update(instr[-8:])
                    return False,self.program_counter
            val=binary_to_decimal(self.program_counter.dump())
            val+=1
            self.program_counter.update(val)
            return False,self.program_counter
        elif(opcode in ['00011','00100']):
            """
            This is the code for load store instructions
            """
            if(opcode=='00011'):
                self.reg_file=load(self.reg_file,self.memory,instr[5:8],instr[-8:])
                val=binary_to_decimal(self.program_counter.dump())
                val+=1
                self.program_counter.update(val)
                return False,self.program_counter
            else:
                self.memory=store(self.reg_file,self.memory,instr[5:8],instr[-8:])
                val=binary_to_decimal(self.program_counter.dump())
                val+=1
                self.program_counter.update(val)
                return False,self.program_counter
        else:
            return True,self.program_counter
