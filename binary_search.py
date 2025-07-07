from re import search
from turtledemo.penrose import start


# binary search
def binary_search(arr, target):
    start_index = 0
    end = len(arr) - 1
    result = -1
    while start_index <= end:
        mid = start_index + (end - start_index) // 2
        if arr[mid] == target:
            result = mid
            break
        elif target > arr[mid]:
            start_index = mid + 1
        else:
            end = mid - 1
    print("Values:", result)


def index_binary_search(arr, target, start_index, end):
    result = -1
    while start_index <= end:
        mid = start_index + (end - start_index) // 2
        if arr[mid] == target:
            result = mid
            break
        elif target > arr[mid]:
            start_index = mid + 1
        else:
            end = mid - 1
    print("Values:", result)


# Find the first occurrence
def binary_search_first_occurrence(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    result = -1
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = arr[mid_index]
        if mid_value == target:
            result = mid_index
            end_index = mid_index - 1
        elif target > mid_value:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    print("First occurrence: ", result)


def binary_search_last_occurrence(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    result = -1
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = arr[mid_index]
        if mid_value == target:
            result = mid_index
            start_index = mid_index + 1
        elif target > mid_value:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    print("First occurrence: ", result)


# find the ceiling no
def binary_search_ceiling_number(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    result = -1
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = arr[mid_index]
        if mid_value == target:
            result = mid_index
        elif target > mid_value:
            start_index = mid_index + 1
        else:
            result = mid_index
            end_index = mid_index - 1
    print("Ceiling Number: ", result)


# find the floor number
def binary_search_floor_number(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    result = -1
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = arr[mid_index]
        if mid_value == target:
            result = mid_index
        elif target > mid_value:
            result = mid_index
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    print("Floor Number: ", result)


# find the floor number
def binary_search_2(arr, target):
    start_index = 0
    end_index = len(arr) - 1
    result = -1
    while start_index <= end_index:
        mid_index = start_index + (end_index - start_index) // 2
        mid_value = arr[mid_index]
        if mid_value == target:
            result = mid_index
        elif target > mid_value:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1

    print("First Number: ", start_index)
    print("End Number: ", end_index)


def infinite_binary_search(arr, target):
    start_index = 0
    end = 1
    while end < len(arr) and target > arr[end]:
        start_index = end
        end = end * 2

    end = min(end, len(arr) - 1)
    index_binary_search(arr, target, start_index, end)


def asc_binary_search(arr, target, start, end):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        mid_value = arr[mid]
        if target == mid_value:
            result = mid
            break
        elif target > mid_value:
            start = mid + 1
        else:
            end = mid - 1

    return result


def desc_binary_search(arr, target, start, end):
    result = -1
    while start <= end:
        mid = start + (end - start) // 2
        mid_value = arr[mid]
        if target == mid_value:
            result = mid
            break
        elif target > mid_value:
            end = mid - 1
        else:
            start = mid + 1

    return result


def find_peek_no(arr):
    start_index = 0
    end = len(arr) - 1
    while start_index <= end:
        mid = start_index + (end - start_index) // 2
        if arr[mid] < arr[mid + 1]:
            start_index = mid + 1
        else:
            end = mid - 1
    return start_index


def search_in_mountain_array(arr, target):
    peek_index = find_peek_no(arr)
    asc_result = asc_binary_search(arr, target, 0, peek_index)
    if asc_result == -1:
        asc_result = desc_binary_search(arr, target, peek_index, len(arr) - 1)
    print(asc_result)


def rotated_array_search(arr, target):
    start_ = 0
    end = len(arr) - 1
    result = -1
    while start_ <= end:
        mid = start_ + (end - start_) // 2
        if target == arr[mid]:
            result = mid
            break
        # to check first part of array is ascending or not if y the
        # then search into the left side
        if arr[start_] <= arr[mid]:
            # checks if target fall into left side of array
            if arr[start_] <= target < arr[mid]:
                end = mid - 1
            else:  # array not found in case left side of array then check the right side of array
                start_ = mid + 1
        else:  # check right side of the array
            if arr[mid] < target <= arr[end]:
                start_ = mid + 1
            else:  # check right side of the array
                end = mid - 1
    print("Values ", result)


def rotated_array_search11(arr, target):
    start_ = 0
    end = len(arr) - 1
    result = -1
    while start_ <= end:
        mid = start_ + (end - start_) // 2
        if target == arr[mid]:
            result = mid
            break
        # to check first part of array is ascending or not if y the
        # then search into the left side
        # check for the duplicate
        if arr[start_] == arr[mid] and arr[mid] == arr[end]:
            start_ + 1
            end - 1
        if arr[start_] <= arr[mid]:
            # checks if target fall into left side of array
            if arr[start_] <= target < arr[mid]:
                end = mid - 1
            else:  # array not found in case left side of array then check the right side of array
                start_ = mid + 1
        else:  # check right side of the array
            if arr[mid] < target <= arr[end]:
                start_ = mid + 1
            else:  # check right side of the array
                end = mid - 1
    print("Values ", result)


def min_no(arr):
    start_ = 0
    end = len(arr) - 1
    min_value = 2_147_483_647
    while start_ <= end:
        mid = start_ + (end - start_) // 2
        if arr[start_] <= arr[mid]:
            min_value = min(min_value, arr[start_])
            start_ = mid + 1
        else:
            min_value = min(min_value, arr[mid])
            end = mid - 1
    print("Min values: ", min_value)


def count_rotated_times(arr):
    start_ = 0
    end = len(arr) - 1
    min_value = 2_147_483_647
    min_index = 2_147_483_647
    while start_ <= end:
        mid = start_ + (end - start_) // 2
        if arr[start_] <= arr[mid]:
            if arr[start_] < min_value:
                min_value = arr[start_]
                min_index = start_
            start_ = mid + 1
        else:
            if arr[mid] < min_index:
                min_value = arr[mid]
                min_index = mid
            end = mid - 1

    print("Rotated values: ", min_index)


# calling methods
# arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr4 = [1, 3, 8, 12, 4, 2]
arr1 = [5, 1, 2, 3, 4]
count_rotated_times(arr1)
