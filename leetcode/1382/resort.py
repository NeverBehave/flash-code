# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return []
        
        self.ls = []
        self.toList(root)
        
        return self.genNode(self.ls)
        
    
    def genNode(self, ls):
        if len(ls) == 0:
            return None
        
        rt = TreeNode()
        mid = (len(ls) - 1) // 2
        
        rt.val = ls[mid]
        if len(ls) > 1:
            rt.left = self.genNode(ls[:mid])
            rt.right = self.genNode(ls[mid+1:])
        
        return rt
        
    
    def toList(self, node):
        if node == None:
            return
        
        self.toList(node.left)
        self.ls.append(node.val)
        self.toList(node.right)
    