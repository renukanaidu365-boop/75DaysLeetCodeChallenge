
from collections import defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        result = 0

        mpp = defaultdict(int)

        mini = n // 2 + 1

        for num in nums:
            mpp[num] += 1
            if mpp[num] == mini:
                result=num

        

        return result
