from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
           
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            char = board[r][c]
            if char == '#' or char not in node.children:
                return
            
            
            node = node.children[char]
            
           
            if node.word:
                result.append(node.word)
                node.word = None 
            
            board[r][c] = '#'
            
          
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            
            
            board[r][c] = char
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        
        return result