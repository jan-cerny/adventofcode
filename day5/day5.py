#!/usr/bin/python3

def execute(program):
    ip = 0
    while True:
        instruction = program[ip]
        instruction_str = f"{instruction:05}"
        p3_imm = bool(int(instruction_str[0]))
        p2_imm = bool(int(instruction_str[1]))
        p1_imm = bool(int(instruction_str[2]))
        opcode = int(instruction_str[3:])
        if opcode == 99:
            return program
        elif opcode in [1, 2]:
            if p3_imm:
                raise ValueError(f"Instruction {instruction_str} has target in immediate mode")
            p1 = program[ip + 1]
            p2 = program[ip + 2]
            target = program[ip + 3]
            if p1_imm:
                op1 = p1
            else:
                op1 = program[p1]
            if p2_imm:
                op2 = p2
            else:
                op2 = program[p2]
            if opcode == 1:
                result = op1 + op2
            elif opcode == 2:
                result = op1 * op2
            program[target] = result
            step = 4
        elif opcode == 3: # input
            target = program[ip + 1]
            input_integer = int(input("Enter an integer: "))
            program[target] = input_integer
            step = 2
        elif opcode == 4: # output
            p1 = program[ip + 1]
            if p1_imm:
                print(p1)
            else:
                print(program[p1])
            step = 2
        elif opcode == 5: # jump-if-true
            p1 = program[ip + 1]
            p2 = program[ip + 2]
            if p1_imm:
                op1 = p1
            else:
                op1 = program[p1]
            if p2_imm:
                op2 = p2
            else:
                op2 = program[p2]
            if op1 != 0: # jump
                ip = op2
                step = 0
            else: # do nothing
                step = 3
        elif opcode == 6: # jump-if-false
            p1 = program[ip + 1]
            p2 = program[ip + 2]
            if p1_imm:
                op1 = p1
            else:
                op1 = program[p1]
            if p2_imm:
                op2 = p2
            else:
                op2 = program[p2]
            if op1 == 0: # jump
                ip = op2
                step = 0
            else: # do nothing
                step = 3
        elif opcode == 7:  # less than
            if p3_imm:
                raise ValueError(f"Instruction {instruction_str} has target in immediate mode")
            p1 = program[ip + 1]
            p2 = program[ip + 2]
            target = program[ip + 3]
            if p1_imm:
                op1 = p1
            else:
                op1 = program[p1]
            if p2_imm:
                op2 = p2
            else:
                op2 = program[p2]
            if op1 < op2:
                result = 1
            else:
                result = 0
            program[target] = result
            step = 4
        elif opcode == 8:  # equals
            if p3_imm:
                raise ValueError(f"Instruction {instruction_str} has target in immediate mode")
            p1 = program[ip + 1]
            p2 = program[ip + 2]
            target = program[ip + 3]
            if p1_imm:
                op1 = p1
            else:
                op1 = program[p1]
            if p2_imm:
                op2 = p2
            else:
                op2 = program[p2]
            if op1 == op2:
                result = 1
            else:
                result = 0
            program[target] = result
            step = 4
        else:
            raise RuntimeError(f"Wrong opcode {opcode}")
        ip += step

def main():
    with open("input", "r") as f:
        contents = f.read().strip()
        program = list(map(int, contents.split(",")))
        execute(program)

if __name__ == "__main__":
    main()
