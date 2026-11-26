class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1 
        for i,c in a.items():
            if c==1:
                return i

        