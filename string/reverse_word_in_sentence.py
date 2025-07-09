from typing import List


def reverse_word_in_sentence(string: str) -> None:
    list_arr: List[str] = string.split(" ")
    res_str: str = ""
    for index in range(len(list_arr) - 1, -1, -1):
        print(list_arr[index])

    print(res_str)
string_data = 'the sky is blue'
reverse_word_in_sentence(string_data)
