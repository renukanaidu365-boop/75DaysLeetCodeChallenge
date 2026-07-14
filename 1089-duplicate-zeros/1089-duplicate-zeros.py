class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        c=0
        a=[]
        for i in range(len(arr)):
                if arr[i]==0:
                    a.append(0)
                    a.append(0)
                else:
                    a.append(arr[i])
        for i in range(len(arr)):
            arr[i]=a[i]
            
        
        