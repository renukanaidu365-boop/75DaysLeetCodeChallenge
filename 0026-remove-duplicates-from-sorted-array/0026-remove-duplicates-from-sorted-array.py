class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f=1
        for s in range(1,len(nums)):
            if nums[s]!=nums[s-1]:
                nums[f]=nums[s]
                f=f+1
        return f
           