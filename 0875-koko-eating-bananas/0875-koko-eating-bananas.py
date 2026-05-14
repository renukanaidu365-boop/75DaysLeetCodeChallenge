import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low=1
        high=max(piles)
        while low<high:
            mid=(low+high)//2
            t=0
            for i in piles:
                t+=math.ceil(i/mid)
            if t<=h:
                high=mid
            else:
                low=mid+1
        return low