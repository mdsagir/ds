def mer(arr, start, end):
    if start == end:
        return
    mid = start + (end - start) // 2
    # left side
    mer(arr, start, mid)
    # right
    mer(arr, mid + 1, end)
    merge_in(arr, start, mid, end)


def merge_in(arr, start, mid, end):
    left = start
    right = mid + 1
    merge = []
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            merge.append(arr[left])
            left += 1
        else:
            merge.append(arr[right])
            right += 1

    while left <= mid:
        merge.append(arr[left])
        left += 1
    while right <= mid:
        merge.append(arr[right])
        right += 1

    for m in range(len(merge)):
        arr[start + m] = merge[m]


in_arr_ = [3, 2, 4, 1, 5, 9]
mer(in_arr_, 0, len(in_arr_) - 1)
print(in_arr_)
