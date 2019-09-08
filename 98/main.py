# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 查看根节点所有的数值都要比根节点数值小
    # 根节点右侧所有数值比根节点数值大
    def isVaild(self, root, min_num, max_num):
        if root == None:
            return True
        if max_num != None and root.val >= max_num: return False
        if min_num != None and root.val <= min_num: return False
        
        return self.isVaild(root.left, min_num, root.val) and self.isVaild(root.right, root.val, max_num)
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isVaild(root, None, None)