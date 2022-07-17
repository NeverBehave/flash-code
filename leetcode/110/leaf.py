# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxlv = -1
        self.res = True
        
        self.recur(root, 0)
        
        return self.res
    
    def recur(self, root, level):
        if self.res == False or root == None:
            return
        
        if root.left == None and root.right == None:
            if self.maxlv == -1:
                self.maxlv = level
                return 
            
            diff = self.maxlv - level 
            if diff > 1 or diff < -1:
                self.res = False
            return
    
        self.recur(root.left, level + 1) 
        self.recur(root.right, level + 1)