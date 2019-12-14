#!/usr/bin/python3

def is_ok(passwd):
    digits = [int(x) for x in str(passwd)]
    if len(digits) != 6:
        return False
    two_adjacent = False
    for i in range(5):
        a = digits[i]
        b = digits[i + 1]
        if a > b:
            return False
        if a == b:
            two_adjacent = True
    return two_adjacent

def test_is_ok():
    assert is_ok(111111)
    assert is_ok(788999)
    assert not is_ok(123)
    assert not is_ok(223450)
    assert not is_ok(123789)

def count_ok(start, stop):
    cnt = 0
    for x in range(start, stop + 1):
        if is_ok(x):
            cnt += 1
    return cnt

def is_ok2(passwd):
    digits = [int(x) for x in str(passwd)]
    if len(digits) != 6:
        return False
    groups = []
    group_len = 1
    for i in range(5):
        a = digits[i]
        b = digits[i + 1]
        if a > b:
            return False
        if a == b:
            group_len += 1
        else:
            groups.append(group_len)
            group_len = 1
    groups.append(group_len)
    return (2 in groups)

def test_is_ok2():
    assert is_ok2(112233)
    assert not is_ok2(123444)
    assert is_ok2(111122)

def count_ok2(start, stop):
    cnt = 0
    for x in range(start, stop + 1):
        if is_ok2(x):
            cnt += 1
    return cnt

if __name__ == "__main__":
    start = 246540
    stop = 787419
    cnt = count_ok(start, stop)
    print(cnt)
    cnt2 = count_ok2(start, stop)
    print(cnt2)