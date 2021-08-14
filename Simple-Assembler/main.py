from functools import reduce
from functionA_F import func_A,func_F
from functionD_E import func_D,func_E
from functionB_C import func_B_C
from set_var_label import set_label_addr,set_var_addr
import error
def check_pnemonic(word,user_input,dict):
    if(word=='var'):
        raise error.IllegalVariable("Variable declared in between")
    lst_A=['add','sub','mul','xor','or','and']
    lst_B_C=['mov','div','ls','rs','cmp','not']
    lst_D=['ld','st']
    lst_E=['jmp','jlt','je','jgt']
    if(word in lst_A):
        return func_A(user_input)
    elif(word in lst_B_C):
        return func_B_C(user_input)
    elif(word in lst_D):
        return func_D(user_input,dict)
    elif(word in lst_E):
        return func_E(user_input,dict)
    else:
        return ""
def main():
    code=""
    while True:
        try:
            line=input()
            code+=line+'\n'
        except EOFError:
            break
    instructions=code.split('\n')
    instructions.pop(len(instructions)-1)
    if('hlt' not in instructions[-1]):
        raise error.IllegalHltInstruction("Hlt instruction missing")
    variables=[]
    i=0
    for i in range(0,len(instructions)):
        instr=instructions[i].split()
        if(instr[0]=='var'):
            variables.append(instructions[i])
        else:
            break
    instructions=instructions[i:]
    dict=set_label_addr(instructions)
    dict2=set_var_addr(variables,len(instructions))
    dict.update(dict2)
    output=""
    for i in range(len(instructions)):
        invid_instr=instructions[i]
        instr=invid_instr.split()
        if(i not in dict.values()):
            val = check_pnemonic(instr[0], invid_instr, dict)
            if(len(val)==0):
                if(instr[0]=='hlt' and i==len(instructions)-1):
                    output+=func_F()
                else:
                    raise error.SyntaxException("Invalid Syntax")
            else:
                output+=val+'\n'
            continue
        instr.pop(0)
        new_invid_instr=reduce(lambda a,b:a+" "+b,instr)
        val=check_pnemonic(instr[0],new_invid_instr,dict)
        if (len(val) == 0):
            if (instr[0] == 'hlt'):
                output += func_F()
            else:
                raise error.SyntaxException("Invalid Syntax")
        else:
            output += val + '\n'
    return output
if(__name__=='__main__'):
    output=main()
    print(output) 
