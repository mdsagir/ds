def first_occurrence(arr, target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            result = mid
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return result


def last_occurrence(arr, target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            result = mid
            start = mid + 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return result


intput_arr = [1, 2, 3, 4, 5, 5, 5, 5, 5, 6, 7, 8]
search_target = 5
res = last_occurrence(intput_arr, search_target)
print(res)
