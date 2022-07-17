# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        self.res = []
        
        self.recur(root, 0)

        return self.res
    
    def recur(self, node, level):
        if node == None:
            return
        
        if len(self.res) == level:
            self.res.append(node.val)
        
        self.recur(node.right, level + 1)
        self.recur(node.left, level + 1)
        