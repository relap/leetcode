class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.minnum = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minstack.append(x)
        if len(self.minnum)==0 or x<self.minnum[-1]:
            self.minnum.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        num = self.minstack[-1]
        self.minstack.pop()
        if self.minnum[-1] == num:
            self.minnum.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minnum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()