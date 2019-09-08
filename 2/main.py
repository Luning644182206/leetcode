# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        re = result
        x = []
        y = []
        while l1 != None or l2 != None:
            if l1 != None:
                x.append(str(l1.val)) 
                l1 = l1.next
            else:
                x.append('0')
                
            if l2 != None:
                y.append(str(l2.val))
                l2 = l2.next
            else:
                y.append('0')
        x_s = ''
        y_s = ''
        while x:
            x_s += x.pop(-1)
            y_s += y.pop(-1)
        
        res = list(str(int(x_s) + int(y_s)))
        
        while res:
            node = ListNode(res.pop(-1))
            re.next = node
            re = re.next
        return result.next