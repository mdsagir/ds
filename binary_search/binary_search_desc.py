def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


input_arr = [12, 10, 8, 6, 3]
search_target = 10
result = binary_search(input_arr, search_target)
print(result)
