class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr=nums
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] + arr[i]
    
        max_sum = float('-inf')
        for i in range(len(arr) - k + 1):
            window_sum = prefix[i+k] - prefix[i]
            max_sum = max(max_sum, window_sum)
    
        return max_sum / k