def floor_with_target(arr, target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if target == arr[mid]:
            result = mid
            break
        elif target > arr[mid]:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


def ceiling_no(arr, target):
    start = 0
    end = len(arr) - 1
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            result = mid
            break
        elif target > arr[mid]:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    return result


input_arr = [1, 2, 5, 8, 12, 15]
search_target = 5
res = ceiling_no(input_arr, search_target)
print(res)
