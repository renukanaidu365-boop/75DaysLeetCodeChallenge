import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a.append((nums[i] * nums[j]) / (math.gcd(nums[i], nums[j]) ** 2))

        return int(max(a))
                