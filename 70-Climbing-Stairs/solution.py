class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        sum = 0
        for i in range(n):
            sum = a + b
            a = b
            b = sum
        return sum
        