from typing import List


def reverse_no(num, rev=0):
    if num == 0:
        return rev

    rev = rev * 10 + num % 10
    return reverse_no(num // 10, rev)


input_no = 123
res = reverse_no(123)


# print(f"{res} is the reverse of {input_no}")

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def is_sorted_rec(arr, i=0):
    if i == len(arr) - 1:
        return True

    return arr[i] < arr[i + 1] and is_sorted_rec(arr, i + 1)


def search(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return search(arr, target, index + 1)


def rotated_search(arr: List[int], target: int) -> int:
    start: int = 0
    end: int = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid

        if arr[start] <= arr[mid]:
            if target >= arr[start] and target <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid] and target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


def rotated_search_rec(arr, target, start, end):
    if start >= end:
        return -1
    mid = start + (end - start)
    if arr[mid] == target:
        return mid
    if arr[start] <= arr[mid]:
        if target >= arr[start] and target <= arr[mid]:
            return rotated_search_rec(arr, target, start, mid - 1)
        else:
            return rotated_search_rec(arr, target, mid + 1, end)
    else:
        if target > arr[mid] and target <= arr[end]:
            return rotated_search_rec(arr, target, mid + 1, end)
        else:
            return rotated_search_rec(arr, target, start, mid - 1)


input_arr = [5, 6, 7, 8, 9, 1, 2, 3]


# print(rotated_search_rec(input_arr, 31, 0, len(input_arr) - 1))

def print_star(num):
    for i in range(1, num + 1):
        for j in range(i, num + 1):
            print("*", end=" ")
        print()


def triangle(r, c):
    if r == 0:
        return
    if r > c:
        print("*", end=" ")
        triangle(r, c + 1)
    else:
        print()
        triangle(r - 1, 0)


def triangle2(r, c):
    if r == 0:
        return
    if r > c:
        triangle2(r, c + 1)
        print("*", end=" ")
    else:
        triangle2(r - 1, 0)
        print()


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(arr)


def bubble_sort_rec(arr, row, col):
    if row == 0:
        return
    if row > col:
        if arr[col] > arr[col + 1]:
            temp = arr[col]
            arr[col] = arr[col + 1]
            arr[col + 1] = temp
        bubble_sort_rec(arr, row, col + 1)
    else:
        bubble_sort_rec(arr, row - 1, 0)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def display_star(r=4, c=0):
    if r == 0:
        return
    if r > c:
        print("*", end=" ")
        display_star(r, c + 1)
    else:
        print()
        display_star(r - 1, 0)


def merge_sort(arr, start, end):
    if start == end:
        return
    mid = start + (end - start) // 2
    # left side
    merge_sort(arr, start, mid)
    # right side
    merge_sort(arr, mid + 1, end)
    merge_in_place(arr, start, mid, end)


def merge_in_place(arr, start, mid, end):
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
    while right <= end:
        merge.append(arr[right])
        right += 1
    for m in range(len(merge)):
        arr[start + m] = merge[m]


in_arr_ = [3, 2, 4, 1, 5, 9]
merge_sort(in_arr_, 0, len(in_arr_) - 1)
print(in_arr_)


def two_sorted_arr(arr1: List[int], arr2: List[int]) -> List[int]:
    i: int = 0
    j: int = 0
    merge: List[int] = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            j += 1

    while i < len(arr1):
        merge.append(arr1[i])
        i += 1
    while j < len(arr2):
        merge.append(arr2[j])
        j += 1
    return merge

# i_arr1 = [1, 2, 3, 4]
# j_arr2 = [5, 6, 7, 8]
# r_arr: List[int] = two_sorted_arr(i_arr1, j_arr2)
# print(r_arr)
