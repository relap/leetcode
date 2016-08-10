class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sl = s.lower()
        sa = ''
        for i in sl:
        	if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
        		sa += i
        strlen = len(sa)

        if strlen %2 ==0:
        	return sa[0:strlen/2] == sa[strlen/2:][::-1]
        else:
        	return sa[0:strlen/2+1] == sa[strlen/2:][::-1]