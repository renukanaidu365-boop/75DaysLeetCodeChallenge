import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        s=0
        s1=0
        for i in range(1,2*n):
            if i%2==0:
                s+=i
            else:
                s1+=i
                
        return math.gcd(s,s1)
            

