#155
# keep tracking the minimum
# The stack will be a stack of pair, each pair will consist of:[value, minimum upto this point]
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or cur_min > val:
            cur_min = val
        self.stack.append((val, cur_min))
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None