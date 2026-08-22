class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g={}
        r={}
        for i in s:
            g[i]=g.get(i,0)+1 
        for i in t:
            r[i]=r.get(i,0)+1 
        if g==r:
            return True
        return False