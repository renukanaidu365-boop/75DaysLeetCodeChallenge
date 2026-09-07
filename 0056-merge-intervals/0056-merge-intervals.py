class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        m=[intervals[0]]
        for i in intervals[1:]:
            l=m[-1]
            if l[1]>=i[0]:
                l[1]=max(l[1],i[1])
            else:
                m.append(i)
        return m