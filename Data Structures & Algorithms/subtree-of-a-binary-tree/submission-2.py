# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True
        
#         if not root and subRoot:
#             return False

#         if self.is_same(root, subRoot):
#             return True
        
#         return (self.is_same(root.left, subRoot) or self.is_same(root.right, subRoot))

#     #Recursive DFS
#     def is_same(self,root,subroot):

#         if not root and not subroot:
#             return True
        
#         if (not root and subroot) or (root and not subroot):
#             return False
        
#         if root and subroot and root.val!=subroot.val:
#             return False
        
#         if root and subroot and root.val==subroot.val :
#             return (self.is_same(root.left,subroot.left) and 
#                     self.is_same(root.right,subroot.right))

        
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.is_same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, root, subroot):
        if not root and not subroot:
            return True
        
        if not root or not subroot:
            return False
        
        if root.val != subroot.val:
            return False
        
        return (
            self.is_same(root.left, subroot.left) and
            self.is_same(root.right, subroot.right)
        )