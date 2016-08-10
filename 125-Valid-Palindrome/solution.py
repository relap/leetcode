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

        for i in range(0,strlen/2):
        	if sa[i] != sa[strlen-1-i]:
        		return False
        return True