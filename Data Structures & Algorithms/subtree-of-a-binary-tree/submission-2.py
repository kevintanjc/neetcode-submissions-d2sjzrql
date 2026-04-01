# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None and q is None:
            return True

        if p is not None and q is not None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        if root is None and subRoot is None:
            return True

        if self.isSameTree(root, subRoot):
            return True
        elif root is not None and subRoot is not None:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return False

        

        