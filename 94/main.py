# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        pop_list = []
        # 左根右
        while root or pop_list:
            # 遍历左子树
            if root:
                # 把左子树左边的点都push进去
                pop_list.append(root)
                root = root.left
            else:
                # 说明没有左边点了
                # 把自己打印
                # 打印右子树
                root = pop_list.pop()
                res.append(root.val)
                root = root.right
        
        
        return res