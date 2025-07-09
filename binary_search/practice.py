import math
from typing import List


def check_eating_banana_speed(piles: List[int], hours: int, max_hour: int) -> int:
    sum_val: int = 0
    for pile in piles:
        sum_val += math.ceil(pile / hours)

    return sum_val <= max_hour


def koko_banana_eating(piles: List[int], max_hour: int) -> int:
    start = 1
    end: int = max(piles)
    while start < end:
        mid: int = start + (end - start) // 2
        if check_eating_banana_speed(piles, mid, max_hour):
            end = mid
        else:
            start = mid + 1
    return start


piles: List[int] = [30,11,23,4,20]
input_hour = 6
res: int = koko_banana_eating(piles, input_hour)
print(res)
