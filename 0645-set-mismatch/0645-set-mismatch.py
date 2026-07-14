class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        b=set()
        n=len(nums)
        d=-1
        for i in nums:
            if i in b:
                d=i
            b.add(i)
        a=n*(n+1)//2 - sum(b)
        return [d,a]