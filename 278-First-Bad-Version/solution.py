# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        minn = 0
        maxn = n - 1
        mid = (minn + maxn) /2 + 1
        while !(isBadVersion(mid) == True and isBadVersion(mid-1) == False):
        	if isBadVersion(mid) == True:
        		maxn = mid
        		mid = (minn + maxn) /2 +1
        	else:
        		minn = mid
        		mid = (minn + maxn) /2 +1
        return mid
        