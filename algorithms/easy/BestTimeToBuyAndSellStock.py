class Solution:
    def maxProfit(self, prices):
        """
        Returns the maximum difference prices[i] - prices[j] where i > j.
        
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('Inf')
        max_difference = 0
        for p in prices:
            if p < min_price:
                min_price = p
            max_difference = max(max_difference, p - min_price)
        return max_difference
