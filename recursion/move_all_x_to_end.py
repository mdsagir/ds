# time complexity O(2N)
# space complexity O(2N)
from typing import List


def move_all_x_to_end(string: str) -> str:
    new_string: str = ""
    count: int = 0
    for s in string:
        if s == 'x':
            count += 1
        else:
            new_string += s
    for index in range(1, count + 1):
        new_string += 'x'
    return new_string


def move_all_x_to_end_rec(string: str, count: int, new_str: str, index: int) -> str:
    if index == len(string):
        for i in range(1, count + 1):
            new_str = new_str + 'x'
        return new_str

    if string[index] == 'x':
        return move_all_x_to_end_rec(string, count + 1, new_str, index + 1)
    else:
        new_str = new_str + string[index]
        return move_all_x_to_end_rec(string, count, new_str, index + 1)


new_s = move_all_x_to_end_rec("ajdfnxxndaxxxxwdnxxsadqw", 0, "", 0)
print(new_s)  # abcdxxx
