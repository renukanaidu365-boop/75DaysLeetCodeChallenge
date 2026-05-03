class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            a.append(nums[i]*nums[i])
        return sorted(a)