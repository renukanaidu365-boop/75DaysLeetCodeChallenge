class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        a = set()
        c = 0
        l = 0
        m = 0
        for r in range(n):
            while nums[r] in a:
                a.remove(nums[l])
                c -= nums[l]
                l += 1
            a.add(nums[r])
            c += nums[r] 
            if r - l + 1 == k:
                m = max(m, c)
                a.remove(nums[l])
                c -= nums[l]
                l += 1
        return m

        

       

