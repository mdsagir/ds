def remove_duplicate(string: str) -> None:
    boo_arr = [False] * 26
    new_string: str = ""

    for index in range(len(string)):
        curr: str = string[index]
        if boo_arr[ord(curr) - ord('a')]:
            continue
        else:
            boo_arr[ord(curr) - ord('a')] = True
            new_string = new_string + curr
    print(new_string)


boo_arr1 = [False] * 26


def remove_duplicate_rec(string: str, new_string: str, index: int) -> str:
    if index == len(string):
        return new_string
    if boo_arr1[ord(string[index]) - ord('a')]:
        return remove_duplicate_rec(string, new_string, index + 1)
    else:
        boo_arr1[ord(string[index]) - ord('a')] = True
        new_string = new_string + string[index]
        return remove_duplicate_rec(string, new_string, index + 1)


r: str = remove_duplicate_rec("axbcxxd", "", 0)
print(r)
