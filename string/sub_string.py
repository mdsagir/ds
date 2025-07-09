def sub_string(string_data: str) -> None:
    l: int = len(string_data) + 1

    for i in range(l):
        for j in range(i + 1, l):
            print(f"{string_data[i:j]}")


string: str = 'abc'
sub_string(string)
