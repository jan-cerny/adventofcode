#!/usr/bin/python3

def test_simple1():
    program = [1,0,0,0,99]
    expected_result = [2,0,0,0,99]
    result = execute(program)
    assert result == expected_result

def test_simple2():
    program = [2,3,0,3,99]
    expected_result = [2,3,0,6,99]
    result = execute(program)
    assert result == expected_result

def test_simple3():
    program = [2,4,4,5,99,0]
    expected_result = [2,4,4,5,99,9801]
    result = execute(program)
    assert result == expected_result

def test_simple4():
    program = [1,1,1,4,99,5,6,0,99]
    expected_result = [30,1,1,4,2,5,6,0,99]
    result = execute(program)
    assert result == expected_result

def test_normal():
    program = [1,9,10,3,2,3,11,0,99,30,40,50]
    expected_result = [3500,9,10,70,2,3,11,0,99,30,40,50]
    result = execute(program)
    assert result == expected_result

def execute(program):
    pc = 0
    while True:
        opcode = program[pc]
        if opcode == 99:
            return program
        elif opcode in [1, 2]:
            src1 = program[pc + 1]
            src2 = program[pc + 2]
            target = program[pc + 3]
            if opcode == 1:
                program[target] = program[src1] + program[src2]
            elif opcode == 2:
                program[target] = program[src1] * program[src2]
        else:
            raise RuntimeError
        pc += 4

def task1(program):
    program[1] = 12
    program[2] = 2
    result = execute(program)
    print(f"Task 1: {result[0]}")

def task2(original):
    noun = 0
    while noun <= 99:
        verb = 0
        while verb <= 99:
            program = original.copy()
            program[1] = noun
            program[2] = verb
            result = execute(program)
            output = result[0]
            if output == 19690720:
                result = 100 * noun + verb
                print(f"Task 2: noun={noun} verb={verb} result={result}")
                return
            verb += 1
        noun += 1

def main():
    with open("input", "r") as f:
        contents = f.read().strip()
        program = list(map(int, contents.split(",")))
        task1(program.copy())
        task2(program.copy())

if __name__ == "__main__":
    main()