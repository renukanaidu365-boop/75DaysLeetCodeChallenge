class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m=0
        s=0
        for i in range(len(gain)):
            s+=gain[i]
            m=max(m,s)
        return m