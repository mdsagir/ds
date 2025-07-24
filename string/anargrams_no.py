from typing import List


def is_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    str1_arr: List[str] = sorted(str1)
    str2_arr: List[str] = sorted(str2)




string: str = 'dabc'
string_res: List[str] = sorted(string)

print(string_res)
