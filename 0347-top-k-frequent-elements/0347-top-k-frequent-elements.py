import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=Counter(nums)
        m=[]
        for n,freq in f.items():
            heapq.heappush(m,(freq,n))
            if len(m)>k:
                heapq.heappop(m)
        t=[]
        while m:
            t.append(heapq.heappop(m)[1])
        return t