class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mstack or val < self.mstack[-1]:
            self.mstack.append(val)
        else:
            self.mstack.append(self.mstack[-1])


    def pop(self) -> None:
        self.mstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
        
