class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=set(candyType)
        b=len(a)
        c=len(candyType)
        d=c//2
        return min(b,d)