import math


def decimal_to_binary(no: int) -> int:
    cnt: int = 0
    res: int = 0
    while no > 0:
        digit: int = no % 2
        no = no // 2
        power: float = math.pow(10, cnt)
        res = int(res + digit * power)
        cnt += 1
    return res



d = decimal_to_binary(235)
# print(d)

print(math.pow(10,0))
print(math.pow(10,1))
print(math.pow(10,2))