class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n & (n-1) == 0 and n != 0:
        	return True
        else:
        	return False 