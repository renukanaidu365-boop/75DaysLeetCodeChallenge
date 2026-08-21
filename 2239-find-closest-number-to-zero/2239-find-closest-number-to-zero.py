class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True) 
        m=0
        a=[]
        for i in range(len(nums)):
            a.append(abs(nums[i]-0))
        mi=a.index(min(a))
        return nums[mi]