class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedNode:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size = self.size + 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size = self.size + 1

    def display(self):
        temp = self.head
        while temp is not None:
            print(str(temp.data) + " -> ", end="")
            temp = temp.next


ln = LinkedNode()
ln.add(10)
ln.add(20)
ln.display()
print(ln.size)
# class Employee:
#     def __init__(self, name, age, mobile, email):
#         self.name = name
#         self.age = age
#         self.mobile = mobile
#         self.email = email
#
#     def print_name(self):
#         print(self.email)
#
#
# employee1 = Employee('John', 32, '2342342342', 'john@gmail.com')
# employee1.print_name()
