from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        res: int = target - nums[i]
        next_value: int = nums[i + 1]
        if res == next_value:
            return [i, i + 1]


    return [-1, -1]

input_arr = [3,2,3]
two_sum_input = 6

r: List[int] = two_sum(input_arr, two_sum_input)
print(r)
