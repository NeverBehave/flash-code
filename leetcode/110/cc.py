# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        self.res = True
        
        self.recur(root, 0)
        

        return self.res
    
    def recur(self, root, level):
        if self.res == False:
            return -1
            
        if root == None:
            return level - 1
        
        l = self.recur(root.left, level + 1)
        r = self.recur(root.right, level + 1)
        
        if abs(l - r) > 1:
            self.res = False
            return -1
        
        return max(l, r)
    
        
        