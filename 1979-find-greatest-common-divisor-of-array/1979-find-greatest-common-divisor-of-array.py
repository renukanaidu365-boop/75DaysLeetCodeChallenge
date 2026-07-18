class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=nums[0]
        b=nums[0]
        for i in range(len(nums)):
            if nums[i]>a:
                a=nums[i]
            if nums[i]<b:
                b=nums[i]
        return gcd(a,b)
