# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(target)

        curr = root
        while curr is not None:
            if curr.val == target:
                break
            elif curr.val < target:
                # right
                if curr.right is not None:
                    curr = curr.right 
                else:
                    curr.right = TreeNode(target)
                    break
            else:
                if curr.left is not None:
                    curr = curr.left
                else:
                    # left
                    curr.left = TreeNode(target)
                    break

        return root

