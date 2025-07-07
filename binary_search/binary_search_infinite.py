def infinite_arra(arr, target):
    start = 0
    end = 1

    while target > arr[end]:
        start = end
        end = end * 2

    print(f"start {start} End {end}")


input_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
infinite_arra(input_arr, 10)
