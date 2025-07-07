def find_min(arr):
    start = 0
    end = len(arr) - 1
    min_val = 2_147_483_647
    while start <= end:
        mid = start + (end - start) // 2
        # for the duplicate element
        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1
        if arr[start] <= arr[mid]:
            min_val = min(min_val, arr[start])
            start = mid + 1
        else:
            min_val = min(min_val, arr[mid])
            end = mid - 1

    return min_val


intput_arr = [4, 5, 6, 7, 2]
res = find_min(intput_arr)
print(res)
