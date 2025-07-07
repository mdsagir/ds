def valid_mountain_array(arr):
    index = 0
    length = len(arr) - 1
    while index < length:
        if arr[index] < arr[index + 1]:
            index += 1
        else:
            break

    if index == 0 or index == length:
        return False

    while index < length:
        if arr[index] > arr[index + 1]:
            index += 1
        else:
            break
    return index == length


input_arr = [1, 2, 3, 4, 5, 1]
res = valid_mountain_array(input_arr)
print(res)
