class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n=len(matrix)
        m=len(matrix[0])

        z_r = [False]*n
        z_c = [False]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    z_r[i] = True
                    z_c[j] = True
        for i in range(n):
            for j in range(m):
                if z_r[i] or z_c[j]:
                    matrix[i][j]=0