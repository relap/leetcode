class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in [3**x for x in range(1000) if 3**x <= n]:
        	return True
        else:
        	return False