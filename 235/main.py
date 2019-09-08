# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 二叉搜索树中比root大的都在右子树
        # 比root小的都在左子树
        # 所以只要比较p,q关系即可
        
        if q.val < root.val and p.val < root.val:
            # 说明两个都在左子树
            return self.lowestCommonAncestor(root.left, p, q)
        if q.val > root.val and p.val > root.val:
            # 说明两个都在右子树
            return self.lowestCommonAncestor(root.right, p, q)
        
        # 如果两个数分开的，说明他们分别在左右子树，说明root就是他们的公共根节点
        return root