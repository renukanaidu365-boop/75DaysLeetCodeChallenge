class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        n=len(height)
        r=n-1
        m=0
        for i in height:
            a=(r-l)*min(height[l],height[r])
            m=max(m,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            
        return m