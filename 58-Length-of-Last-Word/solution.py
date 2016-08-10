class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
        	return 0
        elif s[-1]!=' ':
        	return len(s.split(' ')[-1])
        else:
        	return self.lengthOfLastWord(s[0:-1])

        