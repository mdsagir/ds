def fact(num):
    f = 1
    for index in range(1, num + 1):
        f = f * index
    print(f"factorial of number {num} is {f}")


def fact_rec(num):
    if num == 0:
        return 1
    return num * fact_rec(num - 1)


def sum_of_digit(num):
    sum_ = 0
    for start in range(1, num + 1):
        sum_ += start
    print(sum_)


def sum_of_digi_rec(num, start) -> int:
    if start == num:
        return num

    return start + sum_of_digi_rec(num, start + 1)


def sum_of_digi_rec_2(num) -> int:
    if num == 0:
        return 0

    return num + sum_of_digi_rec_2(num - 1)


def sum_of_digit2(num):
    sum_ = 0
    while not num == 0:
        d = num % 10
        sum_ += d
        num = num // 10
    print(sum_)


def sum_of_digit_rec(num):
    if num == 0:
        return 0

    return num % 10 + sum_of_digit_rec(num // 10)


r = sum_of_digit_rec(321)  # 1 2 3 4


def rev_no(num):
    rev = 0
    while not num == 0:
        rev = rev * 10 + num % 10
        num = num // 10
    print("rev ", rev)


def rev_rec(num, rev=0):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return rev_rec(num // 10, rev)


def count_zero(num, count=0):
    if num == 0:
        return count
    if num % 10 == 0:
        count += 1
    return count_zero(num // 10, count)


def step_to_zero(num):
    cnt = 0
    while not num == 0:
        if num % 2 == 0:
            num = num // 2
            cnt = cnt + 1
        else:
            num = num - 1
            cnt = cnt + 1
    print(cnt)


def step_to_zero_rec(num, count=0):
    if num == 0:
        return count
    if num % 2 == 0:
        num = num // 2
        count = count + 1
    else:
        num = num - 1
        count = count + 1
    return step_to_zero_rec(num, count)



