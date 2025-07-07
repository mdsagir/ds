from typing import List


def binary_search(arr: List[int], target: int) -> int:
    start: int = 0
    end: int = len(arr) - 1
    while start <= end:
        mid: int = start + (end - start) // 2
        mid_value: int = arr[mid]
        if target == mid_value:
            return mid
        elif target > mid_value:
            start = mid + 1
        else:
            end = mid - 1
    return -1


input_arr: List[int] = [12, 33, 42, 55, 65, 73, 89]
search_target: int = 89
result: int = binary_search(input_arr, search_target)
print(result)
