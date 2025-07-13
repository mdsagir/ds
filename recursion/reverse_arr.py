import math
from typing import List


def rev_arr(arr: List[str]) -> None:
    rev(arr, 0)


def rev(arr: List[str], index: int) -> None:
    if index == len(arr) // 2:
        return
    rev(arr, index + 1)
    swap(arr, index, len(arr) - 1 - index)


def swap(arr: List[str], index: int, next_index: int) -> None:
    temp: str = arr[index]
    arr[index] = arr[next_index]
    arr[next_index] = temp


# ca: List[str] = ['h', 'e', 'l', 'l', 'o']
# rev_arr(ca)
# print(ca)
# rev_arr(ca)


def display(no: int) -> None:
    if no > 5:
        return
    print(no)
    display(no + 1)


def sum_of(no, start, sum_):
    if start > no:
        return sum_
    sum_ += start
    return sum_of(no, start + 1, sum_)


def sum_of_(no: int):
    sum_: int = 0
    index: int = 1
    while index <= no:
        sum_ += index  # sum= sum+index
        index += 1  # index ++ or index +1 or index+=1
    print(sum_)


def fact(no: int) -> None:
    f = 1
    for i in range(1, no + 1):
        f = f * i
    print(f)


def fact_rec(no: int, i: int, f: int):
    if i > no:
        return f
    f = f * i
    return fact_rec(no, i + 1, f)


def fact_rec_2(no: int):
    if no == 1 or no == 0:
        return no

    return no * fact_rec_2(no - 1)


# s e sum
# 0 1 1 2 3 5 8
def febo_print(no: int) -> None:
    first: int = 0
    second: int = 1
    print(first)
    print(second)
    for index in range(1, no):
        sum_: int = first + second
        print(sum_)
        first = second
        second = sum_


def febo_rec(no: int, first: int, second: int) -> None:
    if no == 0:
        return
    sum_ = first + second
    # print(sum_)
    febo_rec(no - 1, second, sum_)  # 3 2 1 0
    print(no)


# f = 0
# s = 1
# print(f)
# print(s)
# n = 5
# febo_rec(n - 2, f, s)

# print the power
def power(no: int, pow_: int):
    res: int = 1
    for i in range(1, pow_ + 1):
        res = res * no
    print(res)


def power_rec(no: int, pow_: int) -> int:
    if pow_ == 0:
        return 1
    return no * power_rec(no, pow_ - 1)


def print_rev_string(string: str, index: int) -> None:
    if index >= len(string):
        return
    print_rev_string(string, index + 1)
    print(string[index])


def first_occurrence(string: str, char: str, i: int) -> int:
    if i >= len(string):
        return -1
    if string[i] == char:
        return i
    return first_occurrence(string, char, i + 1)


def last_occurrence(string: str, char: str, i: int, res: int) -> int:
    if i >= len(string):
        return res
    if string[i] == char:
        res = i
    return last_occurrence(string, char, i + 1, res)


input_string: str = "abaacdaefaah"
r: int = last_occurrence(input_string, 'a', 0, -1)
print(r)

# r = power_rec(2, 5)
# print(r)
