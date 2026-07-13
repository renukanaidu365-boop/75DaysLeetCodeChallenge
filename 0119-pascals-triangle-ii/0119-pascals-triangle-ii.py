class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        k=1
        a=[1]
        for i in range(1,rowIndex+1):
            c=k*(rowIndex-i+1)//i
            a.append(c)
            k=c
        return a
        



