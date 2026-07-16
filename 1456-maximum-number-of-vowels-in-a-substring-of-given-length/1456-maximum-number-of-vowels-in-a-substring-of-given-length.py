class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d={'a','e','o','i','u'}
        c=0
        m=0
        for i in range(0,k):
            if s[i] in d:
                c+=1 
        m=c
        for i in range(k,len(s)):
            if s[i] in d:
                c+=1 
            if s[i-k] in d:
                c-=1
            m=max(m,c)
        return m 
