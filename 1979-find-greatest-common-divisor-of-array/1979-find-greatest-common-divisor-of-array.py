class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=sorted(nums)
        b=gcd(a[0],a[-1])
        return b