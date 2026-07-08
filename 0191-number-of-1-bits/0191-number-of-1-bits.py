class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        a=bin(n)[2:]
        for i in range(len(a)):
            if a[i]=='1':
                c+=1 
        return c