class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c = len(grid), len(grid[0])
        count = 0
        
        prefix = [[0] * (c + 1) for _ in range(r + 1)]
        
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        for i in range(r):
            for j in range(c):
                total = prefix[i+1][j+1]
                if total <= k:
                    count += 1
        
        return count
