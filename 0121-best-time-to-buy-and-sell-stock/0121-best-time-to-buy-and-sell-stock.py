class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mi=prices[0]
        m=0
        for i in range(len(prices)):
            if prices[i]<mi:
                mi=min(mi,prices[i])
            a=prices[i]-mi
            m=max(a,m)
        return m