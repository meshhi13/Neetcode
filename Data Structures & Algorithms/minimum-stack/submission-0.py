class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(self.min_val)
        self.min_val = min(self.min_val, val)


    def pop(self) -> None:
        val = self.stack.pop()
        self.min_val = self.min_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_val 
