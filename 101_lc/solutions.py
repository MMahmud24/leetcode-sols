class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        def preorder(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            return (a.val == b.val and preorder(a.left, b.right) and preorder(a.right, b.left))

        
        return preorder(root.left, root.right)
            
