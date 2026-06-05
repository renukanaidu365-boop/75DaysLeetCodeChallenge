class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0,c1,c2=0,0,0
        for i  in nums:
            if i==0: 
                c0+=1 
            elif i==1:
                c1+=1 
            else :
                c2+=1
        for n in range(c0):
            nums[n]=0
        for n in range(c0,c0+c1):
            nums[n]=1 
        for n in range(c0+c1,len(nums)):
            nums[n]=2 