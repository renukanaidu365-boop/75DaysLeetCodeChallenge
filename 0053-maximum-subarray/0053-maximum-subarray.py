class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        
        high=float('-inf')
        cs=0
        for i in range(len(nums)):
            cs=cs+nums[i]
            if high<cs:
               high=cs

            if cs<0:
               cs=0
        return high        
        