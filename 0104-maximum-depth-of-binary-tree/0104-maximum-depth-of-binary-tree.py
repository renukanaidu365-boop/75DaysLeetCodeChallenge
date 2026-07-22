# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        if l==0:
            return r+1 
        if r==0:
            return l+1 
        return 1+max(l,r)
