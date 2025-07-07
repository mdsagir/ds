def if_condition():
    user_name = 'john'
    input_name = input("input your name ")
    if input_name == user_name:
        print("Correct username")
    else:
        print("Opps ! wrong username")


# to validate from in array can use in i in arr, if i inside available inside th array
def if_condition2():
    fruits = ['apple', 'banana']
    input_fruit = input("input fruit ")
    if input_fruit in fruits:
        print("you can buy the fruits")
    else:
        print("fruit is not available")


def for_loop_check():
    arr = [11, 22, 33, 44, 55, 66]
    for index in arr:
        print(index)


for_loop_check()
