def binary_search_order_agnostic(arr, target):
    start = 0
    end = len(arr) - 1
    is_ascending = arr[start] <= arr[end]
    return search(arr, target, is_ascending)


def search(arr, target, is_ascending):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        if is_ascending:
            if target > mid_value:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > mid_value:
                end = mid - 1
            else:
                start = mid + 1
    return -1


input_arr = [1, 2, 3, 4, 5, 6, 7]
search_target = 6
result = binary_search_order_agnostic(input_arr, search_target)
print(result)
