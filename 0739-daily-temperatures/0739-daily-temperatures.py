class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        s=[]
        r=[0]*n
        for i in range(n):
            while s and temperatures[i]>temperatures[s[-1]]:
                p=s.pop()
                r[p]=i-p
            s.append(i)
        return r