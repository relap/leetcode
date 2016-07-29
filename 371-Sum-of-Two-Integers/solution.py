class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b!=0:
            c = a ^ b
            d = (a & b) << 1
            a = c
            b = d
        else:
        	return a