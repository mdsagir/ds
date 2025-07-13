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
            if self.stack[index] is None:
                break
            else:
                print(self.stack[index])

    def stack_size(self):
        return self.top + 1


class Sol:
    @staticmethod
    def minimum_paratheses(string: str) -> int:
        stack = Stack(15)
        for s in string:
            if s == '(':
                stack.push(s)
            else:
                if not stack.is_empty() and stack.peek() == '(':
                    stack.pop()
                else:
                    stack.push(s)
        count: int = 0
        while not stack.is_empty():
            stack.pop()
            count += 1
        return count

    @staticmethod
    def optimize(string: str) -> int:
        start: int = 0
        end: int = 0
        for s in string:
            if s == '(':
                start += 1
            else:
                if not start == 0:
                    start -= 1
                else:
                    end += 1
        return start + end


res: int = Sol.minimum_paratheses(")(()()")
print(f"Results of the programme is {res}")
