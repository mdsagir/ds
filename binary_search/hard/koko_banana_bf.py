from typing import List


def find_max_value(arr: List[int]) -> int:
    max_value: int = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value


def find_ceiling_no(no: float) -> int:
    if no % 1 == 0:
        return int(no)
    else:
        no += 1
        return int(no)


def koko_banana_eating(arr: List[int], hour: int) -> int:
    end: int = find_max_value(arr)
    result: int = -1
    for start in range(1, end + 1):
        total: int = 0
        for a in arr:
            total += find_ceiling_no(a / start)
        if total <= hour:
            result = start
            break
    return result


input_arr: List[int] = [30,11,23,4,20]
input_hour: int = 6
res: int = koko_banana_eating(input_arr, input_hour)
print(res)
