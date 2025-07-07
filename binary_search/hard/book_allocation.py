def is_allocation_possible(books, max_pages, students):
    current_student = 1
    pages = 0
    for i in range(len(books)):
        pages += books[i]
        if pages > max_pages:
            current_student += 1
            pages = books[i]

        if current_student > students:
            return False

    return True


def book_allocation(books, no_of_student):
    if len(books) < no_of_student:
        return -1
    start = 0  # max value of books
    end = 0  # sum of books
    result = -1
    for i in range(len(books)):
        if books[i] > start:
            start = books[i]
        end += books[i]

    while start <= end:
        # max pages that can be allocated to single student
        mid = start + (end - start) // 2

        if is_allocation_possible(books, mid, no_of_student):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


arr = [12, 34, 67, 90]
res = book_allocation(arr, 2)
print(res)
