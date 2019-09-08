# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 没有左节点，那就遍历右子树
        if not root.left: return 1+self.minDepth(root.right)
        
        # 没有右节点，那就遍历左子树
        if not root.right: return 1+self.minDepth(root.left)
        
        # 都存在
        left_deep = self.minDepth(root.left)
        right_deep = self.minDepth(root.right)
        
        return 1+min(left_deep, right_deep)