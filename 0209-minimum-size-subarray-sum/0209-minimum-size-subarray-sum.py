class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l= 0
        c= 0
        min_len = float('inf')
    
        for right in range(len(nums)):
            c += nums[right]
            while c >= target:
                min_len = min(min_len, right - l + 1)
                c -= nums[l]
                l += 1
            
        return min_len if min_len != float('inf') else 0
