class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse="true")
        return nums[k-1]
            