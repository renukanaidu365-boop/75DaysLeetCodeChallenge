class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        c=set(nums)
        m=[]
        for i in range(min(nums)+1,max(nums)):
            if i not in c:
                m.append(i)
        return m