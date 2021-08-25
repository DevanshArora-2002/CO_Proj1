from Execution_engine import ExecutionEngine
from RegisterFile import RegisterRecord
from Program_counter import program_counter
import matplotlib.pyplot as plt
from mem import Memory
from binary_to_decimal import binary_to_decimal
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
    cycles = []
    mem_accesses = []
    while not halted:
        instr=memory.fetch_using_PC(PC.getval(),cycle)
        halted,Next_PC,updated_reg_obj,this_access=execute.execute(instr,PC.getval(),reg_obj,cycle)
        if (len(this_access) > 0):
            cycles.append(cycle)
            cycles.append(cycle)
            mem_accesses.append(PC.getval())
            mem_accesses.append(binary_to_decimal(this_access[0]))
        else:
            cycles.append(cycle)
            mem_accesses.append(PC.getval())
        reg_obj=updated_reg_obj
        PC.dump()
        reg_obj.dump()
        PC.update(Next_PC)
        cycle+=1
    memory.dump()
    print(cycles)
    print(mem_accesses)
    plt.scatter(cycles, mem_accesses)
    plt.xlabel("Cycles")
    plt.ylabel("Memory Addresses")
    plt.savefig("this_plot.png")
if __name__ == "__main__":
    main()
