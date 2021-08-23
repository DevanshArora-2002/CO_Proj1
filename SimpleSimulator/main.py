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
    halted=False
    reg_obj = RegisterRecord()
    memory = Memory()
    memory.initialize(instructions)
    PC = program_counter(0)
    execute = ExecutionEngine(memory, reg_obj.register_file, PC)
    cycle = 0
    while not halted:
        instr=memory.fetch_using_PC(PC.getval(),cycle)
        halted,Next_PC=execute.execute(instr,cycle)
        PC.dump()
        reg_obj.dump()
        PC=Next_PC
    memory.dump()
if __name__ == "__main__":
    main()
