class MinStack:

    s = []
    smallest = 0

    def __init__(self):
        self.s = []
        self.smallest = 2 ** 31 - 1
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if val < self.smallest:
            self.smallest = val
        

    def pop(self) -> None:
        val = self.s.pop()
        if self.smallest == val:
            if len(self.s) == 0:
                self.smallest = 2 ** 31 - 1
            else:
                self.smallest = min(self.s)
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.smallest
        
