class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        ma=nums[0]
        mi=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            t=max(nums[i],ma*nums[i],mi*nums[i])
            mi=min(nums[i],mi*nums[i],ma*nums[i])
            ma=t
            m=max(m,ma)
        return m

      
