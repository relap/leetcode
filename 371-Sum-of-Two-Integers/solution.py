class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD     = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b!=0:
            c = (a ^ b) & MOD
            d = ((a & b) << 1) & MOD
            a = c
            b = d
        else:
        	return a if a <= MAX_INT else ~(a & MAX_INT) ^ MAX_INT