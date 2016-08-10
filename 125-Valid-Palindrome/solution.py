class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sl = s.lower()
        sa = []
        for i in sl:
        	if i>='a' and i<='z' or i>='0' and i<='9':
        		sa.append(i)
        strlen = len(sa)

        for i in range(0,strlen/2):
        	if sa[i] != sa[strlen-1-i]:
        		return False
        return True