from typing import List


class Stack:

    def __init__(self, size: int):
        self.size: int = size
        self.top: int = -1
        self.stack: List[int] = [0] * size

    def push(self, data: int) -> None:
        if self.top >= self.size - 1:
            print("stack is full")
            return
        self.top += 1
        self.stack[self.top] = data

    def is_empty(self) -> bool:
        return self.top <= -1

    def peek(self) -> int:
        if self.is_empty():
            print("stack is empty")
            return -1
        return self.stack[self.top]

    def pop(self) -> int:
        peek: int = self.peek()
        if peek == -1:
            print("stack is empty")
            return -1
        self.top -= 1
        return peek

    def display(self):
        for index in range(0, self.top + 1):
            print(self.stack[index])

    def stack_size(self) -> int:
        return self.top + 1


stack = Stack(5)
stack.push(1)
stack.push(2)
print(stack.stack_size())
