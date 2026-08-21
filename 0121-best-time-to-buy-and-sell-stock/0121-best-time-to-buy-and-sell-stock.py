class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        m=prices[0]
        r=0
        for i in range(1,len(prices)):
            m=min(prices[i],m)
            r=max(r,prices[i]-m)
        return r