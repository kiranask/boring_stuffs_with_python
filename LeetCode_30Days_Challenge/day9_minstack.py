"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

"""

from sys import maxsize
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> None:
        if len(self.lst)>0:
            return self.lst.pop()

    def top(self) -> int:
        if len(self.lst)>0:

            return self.lst[-1]

    def getMin(self) -> int:
        min = maxsize -1
        if len(self.lst) > 0:
            for l in self.lst:
                if l < min:
                    min = l
        return min





#Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(-1)
obj.push(12)
obj.push(20)
obj.push(88)
obj.push(1)
print(obj.pop())
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)