class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ma=0
        for i in range(1,len(nums)):
            if nums[ma]<nums[i]:
                ma=i
        return ma