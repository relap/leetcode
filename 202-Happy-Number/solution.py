class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = []
        while 1 not in res:
        	temp = sum(map(lambda x: x*x, [int(i) for i in str(n)]))
        	if temp == 1:
        		return True
        	elif temp in res:
        		return False
        	res.append(temp)
        	n = temp