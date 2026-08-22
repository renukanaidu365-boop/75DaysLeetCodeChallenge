class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        g={}
        c=0
        for i in text:
           g[i]=g.get(i,0)+1 
        b=g.get('b',0)
        a=g.get('a',0)
        l=g.get('l',0)
        o=g.get('o',0)
        n=g.get('n',0)
        return min(b,a,l//2,o//2,n)

        