# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        pop_list = [root]
        res = []
        # 用栈
        # 先把root打印，再把右孩子放在栈里面
        # 再把左孩子也放栈里面
        # 始终先打印根节点，有左节点就去打印左孩子，直到没有
        # 栈里除了栈顶，都是右节点
        while pop_list:
            root = pop_list.pop()
            res.append(root.val)
            if root.right:
                pop_list.append(root.right)
            if root.left:
                pop_list.append(root.left)
        return res