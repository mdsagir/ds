def find_no_of_rotated(arr):
    start = 0
    end = len(arr) - 1
    min_val = 2_147_483_647
    min_val_index = 2_147_483_647
    while start <= end:
        mid = start + (end - start) // 2
        if arr[start] <= arr[mid]:
            if  arr[start] <= min_val:
                min_val = arr[start]
                min_val_index = start
            start = mid + 1
        else:
            if arr[mid] < min_val:
                min_val = arr[mid]
                min_val_index = mid
            end = mid - 1

    return min_val_index


input_arr = [4, 5, 6, 7, 2]
res = find_no_of_rotated(input_arr)
print(res)
