class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1])) # val vs. currMin

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # get min in O(1)
        # we have a matching minStack that will store all the minimums at each point in our reg stack
        
        # every tiem we push reg stack, we check if we have a new min. Push min to minStack
        # every time we pop reg stack, we pop from minStack -> keeps the stacks matching
        return self.minStack[-1]