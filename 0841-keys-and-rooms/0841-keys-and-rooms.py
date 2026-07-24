class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        a=set()
        def dfs(s):
            a.add(s)
            for i in rooms[s]:
                if i not in a:
                    dfs(i)
        dfs(0)       
        return len(a)==len(rooms)
                    
