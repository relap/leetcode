class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 and 1162261467%n == 0:
        	return True
        else:
        	return False