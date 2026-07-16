import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        p = []
        m = 0
        for i in range(n):
            if nums[i] > m:
                m = nums[i]
            p.append(math.gcd(nums[i], m))
        p.sort()

        ans = 0
        l = 0
        r = len(p) - 1
        while l < r:
            ans += math.gcd(p[l], p[r])
            l += 1 
            r -= 1 
        return ans
