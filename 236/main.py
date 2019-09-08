# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果p或者q就在根节点，说明他的最近公共祖先就是它的根节点
        if root == None or root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左子树是空的，那就说明pq都在右子树
        if left == None and right != None:
            return right
        
        # 如果右子树是空的，那就说明pq都在左子树
        elif left != None and right == None:
            return left
        
        # 如果左右子树都找到了q或者q，那就说明root就是他们的祖先
        elif left != None and right != None:
            return root