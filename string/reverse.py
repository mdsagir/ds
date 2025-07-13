from typing import List


def revers_string_buffer(string: str) -> None:
    newString: str = ""
    for index in range(len(string)):
        newString = string[index] + newString

    print(newString)


def reverse_first_and_last(string: str) -> None:
    arr: List[str] = list(string)
    for index in range(len(arr) // 2):
        temp: str = arr[index]
        arr[index] = arr[(len(arr) - 1) - index]
        arr[(len(arr) - 1) - index] = temp

    print(''.join(arr))


def revers(char_arr: List[str]) -> None:
    for index in range(0, len(char_arr) // 2):
        print(f"{char_arr[index]} and last index {char_arr[(len(char_arr) - 1) - index]}")
    


string_data: str = "helloworld"
ca: List[str] = ['h', 'e', 'l', 'l', 'p']

revers(ca)
