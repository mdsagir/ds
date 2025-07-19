def count_down(n: int):
    if n == 0:
        print("reached 0")
        return

    print("Deeper ", n)
    count_down(n - 1)
    print("Count down", n)


def iterative(n):
    for i in range(n, -1, -1):
        print("Deeper ", i)
    for i in range(1, n + 1):
        print("Count down", i)






def subset(n, path: str):
    if n == 2:
        print(path)
        return

    subset(n + 1, path + "0")
    subset(n + 1, path + "1")


subset(0, "")

def subset1():
    subset2("0")
    subset2("1")

def subset2(path):
    subset3(path + "0")
    subset3(path + "1")

def subset3(path):
    print(path)

# Start the chain
# subset1()