class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        l,r=0,len(a)-1 
        while l<r:
            a[l],a[r]=a[r],a[l]
            l+=1 
            r-=1 
        return " ".join(a)


