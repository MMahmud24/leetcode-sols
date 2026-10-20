class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.index = 0
        self.ordered = self.inOrder(root)

    def inOrder(self, root):
        res = [[0]]

        def traversal(root):
            if not root:
                return
            
            traversal(root.left)
            res[0].append(root)
            traversal(root.right)

        
        traversal(root)
        return res[0][1:]

    def next(self) -> int:
        value = self.ordered[self.index].val
        self.index+=1
        return value

    def hasNext(self) -> bool:
        if self.index == len(self.ordered):
            return False
        
        return True
