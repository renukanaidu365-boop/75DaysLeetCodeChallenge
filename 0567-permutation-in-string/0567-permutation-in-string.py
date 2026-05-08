class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = [0] * 26
        for c in s1:
            count[ord(c) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            temp = count.copy()
            for j in range(len(s1)):
                temp[ord(s2[i + j]) - ord('a')] -= 1
            if all(x == 0 for x in temp):
                return True
        
        return False