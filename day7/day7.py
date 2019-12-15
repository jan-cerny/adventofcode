#!/usr/bin/python3

from itertools import permutations

def execute(program, inputs):
    ip = 0
    while True:
        instruction = program[ip]
        instruction_str = f"{instruction:05}"
        p3_imm = bool(int(instruction_str[0]))
        p2_imm = bool(int(instruction_str[1]))
        p1_imm = bool(int(instruction_str[2]))
        opcode = int(instruction_str[3:])
        if opcode == 99:
            return
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
            input_integer = inputs.pop(0)
            program[target] = input_integer
            step = 2
        elif opcode == 4: # output
            p1 = program[ip + 1]
            if p1_imm:
                output = p1
            else:
                output = program[p1]
            new_input = yield output
            inputs.append(new_input)
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

def load_program_from_input_file():
    with open("input", "r") as f:
        contents = f.read().strip()
        program = list(map(int, contents.split(",")))
        return program

def amplify(program, phase_settings):
    signal = 0
    for i in range(5):
        amplifier_inputs = [phase_settings[i], signal]
        amplifier = execute(program, amplifier_inputs)
        signal = next(amplifier)
    return signal

def test_amplify_1():
    program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    phase_settings = [4,3,2,1,0]
    assert amplify(program, phase_settings) == 43210

def test_amplify_2():
    program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    phase_settings = [0,1,2,3,4]
    assert amplify(program, phase_settings) == 54321

def test_amplify_3():
    program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
        1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    phase_settings = [1,0,4,3,2]
    assert amplify(program, phase_settings) == 65210

def find_max(program):
    max_thruster_signal = 0
    for phase_settings in permutations(range(5)):
        thruster_signal = amplify(program, phase_settings)
        if thruster_signal > max_thruster_signal:
            max_thruster_signal = thruster_signal
    return max_thruster_signal

def feedback(program, phase_settings):
    signal = 0
    amplifiers = []
    for i in range(5):
        amplifier_inputs = [phase_settings[i], signal]
        amplifier = execute(program, amplifier_inputs)
        amplifiers.append(amplifier)
        signal = next(amplifier)
    while True:
        for a in amplifiers:
            try:
                signal = a.send(signal)
            except StopIteration:
                return signal

def find_max_feedback(program):
    max_thruster_signal = 0
    for phase_settings in permutations(range(5, 9 + 1 )):
        thruster_signal = feedback(program, phase_settings)
        if thruster_signal > max_thruster_signal:
            max_thruster_signal = thruster_signal
    return max_thruster_signal

def main():
    program = load_program_from_input_file()
    max_thruster_signal = find_max(program)
    print(f"The highest signal that can be sent to the thrusters is {max_thruster_signal}")
    max_thruster_signal_feedback = find_max_feedback(program)
    print(f"The highest signal that can be sent to the thrusters using feedback loop is {max_thruster_signal_feedback}")



if __name__ == "__main__":
    main()
