def brute_force(arr):
    index = 1
    length = len(arr) - 1
    peek = -1
    while index < length:
        if arr[index] > arr[index - 1] and arr[index] > arr[index + 1]:
            peek = index
            break
        index += 1
    return peek


def binary_search(arr):
    start = 0
    end = len(arr) - 1
    length = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if mid != 0 and mid != length and arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return mid
        elif mid != length and arr[mid] > arr[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


input_arr = [1, 2, 3, 4, 5, 6, 5, 4]
peek_e = binary_search(input_arr)
print(peek_e)
