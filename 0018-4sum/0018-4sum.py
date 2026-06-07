class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()  
        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    required = target - nums[i] - nums[j] - nums[k] 

                    if required in seen:
                        temp = tuple(sorted([nums[i], nums[j], nums[k], required]))
                        st.add(temp)

                    seen.add(nums[k])

        return [list(quad) for quad in st]


