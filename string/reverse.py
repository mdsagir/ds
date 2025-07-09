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


string_data: str = "helloworld"

reverse_first_and_last(string_data)
