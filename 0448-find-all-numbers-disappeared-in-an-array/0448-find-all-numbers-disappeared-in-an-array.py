class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=set(nums)
        f=[]
        for i in range(1,n+1):
            if i not in a:
                f.append(i)
        return f