class Solution:
    def rob(self, nums: List[int]) -> int:
        h1=0
        h2=0
        for i in nums:
            t=max(h1+i,h2)
            h1=h2
            h2=t
        return h2