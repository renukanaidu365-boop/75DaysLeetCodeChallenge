class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        r=[]
        while i<len(word1) and j<len(word2):
            r.append(word1[i])
            r.append(word2[i])
            i+=1 
            j+=1 
        r.append(word1[i:])
        r.append(word2[j:])
        return ''.join(r)
        