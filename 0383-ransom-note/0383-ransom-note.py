class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=list(magazine)
        c=0
        for i in ransomNote:
            if i in a:
                c+=1 
                a.remove(i)
        if len(ransomNote)<=c:
            return True
        return False