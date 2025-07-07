import math
from typing import List


def practice(arr):
    max_student = 2
    max_page = 50
    pages = 0
    current_student = 1
    for i in range(len(arr)):
        pages += arr[i]
        if pages > max_page:
            current_student += 1
            pages = arr[i]
        print("current_student ", current_student, " pages ", pages)
        if current_student > max_student:
            break


def koko_banana(arr: List[int], hour: int) -> int:
    result: int = -1
    end: int = max(arr)
    for i in range(1, end + 1):
        sum_: int = 0
        for index in range(len(arr)):
            r = math.ceil(arr[index] / i)
            sum_ += r

        if sum_ <= hour:
            result = i
            break

    return result


input_arr: List[int] = [30, 11, 23, 4, 20]
res: int = koko_banana(input_arr, 6)
print(res)
