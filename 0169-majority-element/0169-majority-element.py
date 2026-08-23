
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ca=None
        c=0
        for i in nums:
            if c==0:
                ca=i 
            c+=1 if ca==i else -1
        return ca