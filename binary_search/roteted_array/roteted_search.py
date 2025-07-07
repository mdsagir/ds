def rotated_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        # for the checking the duplicate element
        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1
        if arr[start] <= arr[mid]:
            if target >= arr[start] and target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid] and target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


input_arr = [1, 0, 1, 1, 1, 1]
target_input = 10
res = rotated_search(input_arr, target_input)
print(res)

# steps 1:  Check which side of the array is sorted
#           find the middle check if start is less then equals middle means sorted
#           if found in left side then check target is lie in between or not
