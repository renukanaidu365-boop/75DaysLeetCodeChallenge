class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        r=[]
        for i in nums1:
            b=False
            a=nums2.index(i)
            for j in range(a+1,len(nums2)):
                if nums2[j] > i:
                    r.append(nums2[j])
                    b=True
                    break
            else:
                r.append(-1)
        return r


        