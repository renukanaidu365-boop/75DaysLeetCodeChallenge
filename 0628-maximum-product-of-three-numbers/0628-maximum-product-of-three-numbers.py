class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        m=0
        nums.sort()
        a=nums[-1]*nums[-2]*nums[-3]
        b=nums[-1]*nums[0]*nums[1]
        return max(a,b)