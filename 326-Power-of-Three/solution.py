class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%10 not in [1,3,7,9]:
        	return False
        else:
	        if n in [3**x for x in range(1000) if 3**x <= n]:
	        	return True
	        else:
	        	return False