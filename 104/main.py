# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 加1是因为本节点也算一层
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    