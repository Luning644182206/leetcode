# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # 后序打印二叉树（非递归）
    # 使用两个栈结构
    # 第一个栈进栈顺序：左节点->右节点->跟节点
    # 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
    # 第二个栈存储为第一个栈的每个弹出依次进栈
    # 最后第二个栈依次出栈
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        
        pop_list_in = [root]
        pop_list_out = []
        while pop_list_in:
            root = pop_list_in.pop()
            pop_list_out.append(root)
            if root.left:
                pop_list_in.append(root.left)
            if root.right:
                pop_list_in.append(root.right)
        
        while pop_list_out:
            root = pop_list_out.pop()
            res.append(root.val)
        return res
        