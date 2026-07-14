class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        
        c=0
        d=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1 
        for x in range(len(nums)-c):
            if nums[x]==0:
                d+=1 
        return d