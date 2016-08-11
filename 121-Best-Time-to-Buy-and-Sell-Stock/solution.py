class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
        	return 0
        profit = 0
        minn = prices[0]
        for i in range(1,len(prices)):
        	if prices[i]<minn:
        		minn = prices[i]
        	if prices[i]-minn>profit:
        		profit = prices[i]-minn
        return profit