class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)       
        n = len(grid[0])    
        
        re = [[0] * n for _ in range(m)]
        total = m * n

        k %= total

        for r in range(m):
            for c in range(n):

                old=r * n + c
                
                new=(old + k) % total
                
                new_r=new // n
                new_c=new % n

                re[new_r][new_c]=grid[r][c]
                
        return re



