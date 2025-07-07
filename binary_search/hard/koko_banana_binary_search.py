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

def check_to_eat_in_time(piles: List[int], hour: int, speed: int) -> bool:
    sum_res: int = 0
    for pile in piles:
        sum_res += find_ceiling_no(pile / speed)
    return sum_res <= hour


def koko_banana_eating(arr: List[int], hour: int) -> int:
    start: int = 1
    end: int = find_max_value(arr)
    while start < end:
        mid: int = start + (end - start) // 2
        if check_to_eat_in_time(arr, hour, mid):
            end = mid
        else:
            start = mid + 1
    return start


input_arr: List[int] = [30, 11, 23, 4, 20]
input_hour: int = 5
res: int = koko_banana_eating(input_arr, input_hour)
print(res)
