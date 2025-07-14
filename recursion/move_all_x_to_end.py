# time complexity O(2N)
# space complexity O(2N)
def move_all_x_to_end(string: str) -> str:
    new_string: str = ""
    count: int = 0
    for s in string:
        if s == 'x':
            count += 1
        else:
            new_string += s
    for index in range(1, count + 1):
        new_string += 'x'
    return new_string




new_s = move_all_x_to_end("axbcxxd")
print(new_s)  # abcdxxx
