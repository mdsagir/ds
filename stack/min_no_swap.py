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


class MinSwap:
    @staticmethod
    def min_swap(string: str) -> int:
        if not len(string) % 2 == 0:
            return -1
        open: int = 0
        close: int = 0
        for s in string:
            if s == '[':
                open += 1
            else:
                if not open == 0:
                    open -= 1
                else:
                    close += 1
        open_close: int = (open + close) / 2
        res: int = int((open_close + 1) / 2)

        return res


r: int = MinSwap.min_swap("]]]]]][[[[[[")
print(r)
