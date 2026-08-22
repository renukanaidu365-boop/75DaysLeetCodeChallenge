class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c=0
        a=set(jewels)
        for i in stones:
            if i in a:
                c+=1
        return c