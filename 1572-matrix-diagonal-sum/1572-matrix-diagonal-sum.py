class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        a=0
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    a += mat[i][j]
        return a
        