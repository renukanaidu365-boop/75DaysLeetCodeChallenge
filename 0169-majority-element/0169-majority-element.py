class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1 
        for i,c in a.items():
            if c>n//2:
                return i
