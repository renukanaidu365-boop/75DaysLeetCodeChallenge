class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ch=[]
        for i in range(len(s)-1,-1,-1):
            ch.append(s[i])
        for i in range(len(s)):
            s[i]=ch[i]