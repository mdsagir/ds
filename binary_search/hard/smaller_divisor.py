import math
from typing import List


def smaller_divisor(arr: List[int], threshold: int) -> int:
    max_value: int = max(arr)

    for r in range(1, max_value + 1):
        sum_value = 0
        for ar in arr:
            sum_value += math.ceil(ar / r)
        if sum_value <= threshold:
            return r
    return -1


def is_division_possible(arr: List[int], divisor: int, threshold: int) -> bool:
    result: int = 0
    for a in arr:
        result += math.ceil(a / divisor)
    return result <= threshold


def smaller_divisor_binary_search(arr: List[int], threshold: int) -> int:
    end: int = max(arr)
    start = 1
    result: int = -1
    while start <= end:
        mid: int = start + (end - start) // 2
        if is_division_possible(arr, mid, threshold):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


input_arr: List[int] = [44,22,33,11,1]
res: int = smaller_divisor_binary_search(input_arr, 5)
print(res)
