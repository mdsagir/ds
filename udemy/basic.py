from typing import List

age: int = 35
PI: float = 3.14

my_string = "Hello \"World\""
my_string2 = 'Hello \'World\''
my_string3 = """
{ 
    id:123,
    name:"John"
    }
"""
print(my_string)
print(my_string2)
print(my_string3)

# covert int to str
age = 32
age_as_string = str(32)

print(age_as_string)

roll = "21"
roll_as_int = int(roll)
print(roll)
print(roll_as_int)

print(type(10))
print(type("10"))
print(type(10.10))
print(type(1==2))
print(type(List[int]))