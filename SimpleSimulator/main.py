from Execution_engine import ExecutionEngine
from RegisterFile import RegisterRecord
from Program_counter import program_counter
from mem import Memory
def main():
    instructions = []
    while True:
        try:
            instructions.append(input())
        except EOFError:
            break
    halted = False
    reg_obj = RegisterRecord()
    memory = Memory()
    memory.initialize(instructions)
    PC = program_counter(0)
    execute = ExecutionEngine(memory, PC)
    cycle = 0
    accesses = {}
    while not halted:
        instr=memory.fetch_using_PC(PC.getval(),cycle)
        halted,Next_PC,updated_reg_obj,this_access=execute.execute(instr,PC.getval(),reg_obj,cycle)
        reg_obj=updated_reg_obj
        PC.dump()
        reg_obj.dump()
        PC.update(Next_PC)
        accesses.update(this_access)
    memory.dump()
if __name__ == "__main__":
    main()
