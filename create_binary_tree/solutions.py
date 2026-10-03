# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        
        nodes_dict = {}
        children = set()
        for desc in descriptions:
            if desc[0] not in nodes_dict:
                curr_root = TreeNode(desc[0])
                nodes_dict[desc[0]] = curr_root
            else:
                curr_root = nodes_dict.get(desc[0])
                
            if desc[1] not in nodes_dict:
                child = TreeNode(desc[1])
                nodes_dict[desc[1]] = child
            else:
                child = nodes_dict.get(desc[1])
                
            if desc[2] == 1:
                curr_root.left = child
            else:
                curr_root.right = child

            children.add(desc[1])


        parent = None
        for key in nodes_dict.keys():
            if key not in children:
                parent = nodes_dict.get(key)
                break

        return parent


            
