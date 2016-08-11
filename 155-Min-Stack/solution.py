class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minstack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.minstack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()