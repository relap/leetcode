class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1 :
            return True
        elif num&(num-1) == 0 and (num%10 in [4,6]):
            return True
        else:
            return False
            