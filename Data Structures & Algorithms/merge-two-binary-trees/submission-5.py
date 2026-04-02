# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return

        root = TreeNode()

        def buildTree(root1: Optional[TreeNode], root2: Optional[TreeNode], buildRoot: Optional[TreeNode]):
            if root1 is None and root2 is None:
                return
            if root1 is None:
                # only root2 has a subtree
                buildRoot.val = root2.val
                if root2.left is None and root2.right is None:
                    #root2 has no left or right subtree i terminate
                    return
                elif root2.left is None:
                    #root2 has a right subtree only
                    new_right = TreeNode()
                    buildRoot.right = new_right
                    buildTree(None, root2.right, new_right)
                elif root2.right is None:
                    #root2 has a left subtree only
                    new_left = TreeNode()
                    buildRoot.left = new_left
                    buildTree(None, root2.left, new_left)
                else:
                    #root2 has both left and right subtrees
                    new_right = TreeNode()
                    buildRoot.right = new_right
                    buildTree(None, root2.right, new_right)
                    new_left = TreeNode()
                    buildRoot.left = new_left
                    buildTree(None, root2.left, new_left)
            elif root2 is None:
                # only root1 has a subtree
                buildRoot.val = root1.val
                if root1.left is None and root1.right is None:
                    #root1 has no left or right subtree i terminate
                    return
                elif root1.left is None:
                    #root1 has a right subtree only
                    new_right = TreeNode()
                    buildRoot.right = new_right
                    buildTree(root1.right, None, new_right)
                elif root1.right is None:
                    #root1 has a left subtree only
                    new_left = TreeNode()
                    buildRoot.left = new_left
                    buildTree(root1.left, None, new_left)
                else:
                    #root1 has both left and right subtrees
                    new_right = TreeNode()
                    buildRoot.right = new_right
                    buildTree(root1.right, None, new_right)
                    new_left = TreeNode()
                    buildRoot.left = new_left
                    buildTree(root1.left, None, new_left)
            else:
                #both roots are present
                buildRoot.val = root1.val + root2.val
                if root1.left is not None or root2.left is not None:
                    new_left = TreeNode()
                    buildRoot.left = new_left
                    buildTree(root1.left, root2.left, new_left)
                if root1.right is not None or root2.right is not None:
                    new_right = TreeNode()
                    buildRoot.right = new_right
                    buildTree(root1.right, root2.right, new_right)
            
            return


        buildTree(root1, root2, root)

        return root

            