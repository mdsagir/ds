from typing import List


def is_array_sorted(arr: List[int]) -> bool:
    for index in range(len(arr) - 1):
        if not arr[index] < arr[index + 1]:
            return False
    return True


def rec_is_arr_sorted(arr: List[int], index: int) -> bool:
    if index == len(arr) - 1:
        return True
    if arr[index] < arr[index + 1]:
        return rec_is_arr_sorted(arr, index + 1)
    else:
        return False


input_arr: List[int] = [1, 2, 3, 4, 5]
r: bool = rec_is_arr_sorted(input_arr,0)
print(r)
