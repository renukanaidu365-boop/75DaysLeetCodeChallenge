class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        f=True
        while l<r:
            re=numbers[l]+numbers[r]
            if target==re:
               return (l+1,r+1)
               f=False
               break
            elif target<re:
               r=r-1
            else:
                l=l+1
        if f:
            return -1,-1