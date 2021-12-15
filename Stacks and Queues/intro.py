# STACK
class PlateStack:
    def __init__(self):
        self.st = []
    def push(self, x: int) -> None:
        self.st.append(x)
    def pop(self) -> None:
        if(len(self.st) > 0):
            self.st.pop()
    def top(self) -> int:
        if(len(self.st) == 0):
            return None
        return self.st[-1]
    def getLen(self) -> int:
      return len(self.st)
#QUEUE
class QueueLine:
    def __init__(self):
        self.q = []
    def enqueue(self, x):
        self.q.append(x)
    def dequeuq(self):
        if (len(self.q) > 0):
            self.q.pop(0)
    def front(self):
        if (len(self.q) == 0):
            return None
        return self.q[0]
#QUEUE
class QueueLine:
    def __init__(self):
        self.q = []
    def enqueue(self, x):
        self.q.append(x)
    def dequeuq(self):
        if (len(self.q) > 0):
            self.q.pop(0)
    def front(self):
        if (len(self.q) == 0):
            return None
        return self.q[0]