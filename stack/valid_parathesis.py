from typing import List


class Stack:

    def __init__(self, size: int):
        self.size: int = size
        self.top: int = -1
        self.stack: List[str] = [""] * size

    def push(self, data: str) -> None:
        if self.top >= self.size - 1:
            print("stack is full")
            return
        self.top += 1
        self.stack[self.top] = data

    def is_empty(self) -> bool:
        return self.top <= -1

    def peek(self) -> str:
        if self.is_empty():
            print("stack is empty")
            return ''
        return self.stack[self.top]

    def pop(self) -> str:
        peek: str = self.peek()
        if peek == '':
            print("stack is empty")
            return ''
        self.top -= 1
        return peek

    def display(self):
        for index in range(0, self.top + 1):
            print(self.stack[index])

    def stack_size(self):
        return self.top + 1


class ValidParathesis:
    @staticmethod
    def check_valida_parathesis(string: str) -> bool:
        if len(string) % 2 != 0:
            return False
        stack = Stack(10)
        for s in string:
            if s == '(' or s == '{' or s == '[':
                stack.push(s)
            else:
                if stack.is_empty():
                    return False
                peek: str = stack.peek()

                if s == ')' and peek == '(':
                    stack.pop()
                elif s == '}' and peek == '{':
                    stack.pop()
                elif s == ']' and peek == '[':
                    stack.pop()
                else:
                    return False

        return stack.stack_size() == 0


status: bool = ValidParathesis.check_valida_parathesis("([]")
print(status)
