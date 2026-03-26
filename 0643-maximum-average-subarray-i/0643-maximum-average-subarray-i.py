class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        arr=nums
        p= [0] * (len(arr) + 1)
        for i in range(len(arr)):
            p[i+1] = p[i] + arr[i]
    
        max_sum = float('-inf')
        for i in range(len(arr) - k + 1):
            window_sum = p[i+k] - p[i]
            max_sum = max(max_sum, window_sum)
    
        return max_sum /k
        