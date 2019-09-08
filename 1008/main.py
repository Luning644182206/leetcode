# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findNullPosition(self, node_index, tree_node, num):
        node = tree_node[node_index]
        if node.val > num:
            if node.left == None:
                node.left = len(tree_node)
                tree_node.append(TreeNode(num))
            else:
                self.findNullPosition(node.left, tree_node, num)
        if node.val < num:
            if node.right == None:
                node.right = len(tree_node)
                tree_node.append(TreeNode(num))
            else:
                self.findNullPosition(node.right, tree_node, num)

    def showAllNodes(self, node_index, tree_node, result):
        # if node_index == None:
        #     return
        # print(tree_node[node_index].val)
        # self.showAllNodes(tree_node[node_index].left, tree_node)
        # self.showAllNodes(tree_node[node_index].right, tree_node)
        need_show_index = []
        none_num = 0
        for item in node_index:
            if item == None:
                none_num += 1

        if none_num != len(node_index):
            for index in node_index:
                if index != None:
                    print(tree_node[index].val)
                    result.append(tree_node[index].val)
                    need_show_index.append(tree_node[index].left)
                    need_show_index.append(tree_node[index].right)
                else:
                    result.append(None)
                    print(None)
            self.showAllNodes(need_show_index, tree_node, result)
        
    def fixResult(self, arr):
        len_result = len(arr)
        if arr[len_result - 1] == None:
            arr.pop(-1)
            self.fixResult(arr)


    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        # left_index = 0
        # right_index = 0
        counter = 0
        # num_hash = {}
        # root_node = preorder[0]
        tree_node = []
        result = []
        for index,item in enumerate(preorder):
            if len(tree_node) > 0:
                self.findNullPosition(0, tree_node, item) 
            else:
                node = TreeNode(item)
                tree_node.append(node)
        self.showAllNodes([0], tree_node, result)
        self.fixResult(result)

        return result 


if __name__ == '__main__':
    a = [4,2]
    # a = [8,5,1,7]
    b = Solution()
    
    print(b.bstFromPreorder(a))
    # a = [1,1,1,1,None]
    # print()





