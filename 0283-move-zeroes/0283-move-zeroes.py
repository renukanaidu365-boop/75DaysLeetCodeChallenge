class Solution(object):
    def moveZeroes(self, nums):
        a=[]
        b=[]
        r=""
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        r=b+a
        for i in range(n):
            nums[i]=r[i]
        return nums[i]