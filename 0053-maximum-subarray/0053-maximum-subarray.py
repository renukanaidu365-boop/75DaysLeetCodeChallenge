class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ma=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            ma=max(nums[i],ma+nums[i])
            m=max(m,ma)
        return m