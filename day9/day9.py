#!/usr/bin/python3

from collections import defaultdict

position_mode = 0
immediate_mode = 1
relative_mode = 2

def fetch_operand(program, ip, relative_base, position, mode):
    parameter = program[ip + position]
    if mode == position_mode:
        operand = program[parameter]
    elif mode == immediate_mode:
        operand = parameter
    elif mode == relative_mode:
        operand = program[relative_base + parameter]
    else:
        raise ValueError(f"Unknown mode {mode}")
    return operand

def get_target_address(program, ip, relative_base, position, mode):
    if mode == position_mode:
        target_address = program[ip + position]
    elif mode == immediate_mode:
        raise ValueError("Instruction has target in immediate mode")
    elif mode == relative_mode:
        target_address = relative_base + program[ip + position]
    else:
        raise ValueError(f"Unknown mode {mode}")
    return target_address

def execute(program):
    ip = 0
    relative_base = 0
    while True:
        instruction = program[ip]
        instruction_str = f"{instruction:05}"
        p3_mode = int(instruction_str[0])
        p2_mode = int(instruction_str[1])
        p1_mode = int(instruction_str[2])
        opcode = int(instruction_str[3:])
        if opcode == 99:
            return program
        elif opcode in [1, 2, 7, 8]:
            op1 = fetch_operand(program, ip, relative_base, 1, p1_mode)
            op2 = fetch_operand(program, ip, relative_base, 2, p2_mode)
            if opcode == 1: # add 
                result = op1 + op2
            elif opcode == 2: # sub
                result = op1 * op2
            elif opcode == 7:  # less than
                if op1 < op2:
                    result = 1
                else:
                    result = 0
            elif opcode == 8:  # equals
                if op1 == op2:
                    result = 1
                else:
                    result = 0
            target_address = get_target_address(program, ip, relative_base, 3, p3_mode)
            program[target_address] = result
            step = 4
        elif opcode == 3: # input
            input_integer = int(input("Enter an integer: "))
            target_address = get_target_address(program, ip, relative_base, 1, p1_mode)
            program[target_address] = input_integer
            step = 2
        elif opcode == 4: # output
            value = fetch_operand(program, ip, relative_base, 1, p1_mode)
            print(value)
            step = 2
        elif opcode == 5: # jump-if-true
            op1 = fetch_operand(program, ip, relative_base, 1, p1_mode)
            op2 = fetch_operand(program, ip, relative_base, 2, p2_mode)
            if op1 != 0: # jump
                ip = op2
                step = 0
            else: # do nothing
                step = 3
        elif opcode == 6: # jump-if-false
            op1 = fetch_operand(program, ip, relative_base, 1, p1_mode)
            op2 = fetch_operand(program, ip, relative_base, 2, p2_mode)
            if op1 == 0: # jump
                ip = op2
                step = 0
            else: # do nothing
                step = 3
        elif opcode == 9:
            op1 = fetch_operand(program, ip, relative_base, 1, p1_mode)
            relative_base += op1
            step = 2
        else:
            raise RuntimeError(f"Wrong opcode {opcode}")
        ip += step

def string_to_program(prstr):
    program = defaultdict(int, enumerate(map(int, prstr.split(","))))
    return program

def main():
    with open("input", "r") as f:
        contents = f.read().strip()
        program = string_to_program(contents)
        execute(program)

if __name__ == "__main__":
    main()
