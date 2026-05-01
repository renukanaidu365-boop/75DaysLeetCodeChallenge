class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        t=0
        d={}
        c=0
        for i in range(len(nums)):
            t+=nums[i]
            if t==k:
                c+=1
            if (t-k) in d:
                c+=d[t-k]
            if t in d:
                d[t]+=1
            else:
                d[t]=1
        return c