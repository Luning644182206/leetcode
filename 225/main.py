from queue import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_stack = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue_stack.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        size = self.queue_stack.qsize() - 1
        result = None

        while size:
            data = self.queue_stack.get()
            self.queue_stack.put(data)
            size -= 1
        result = self.queue_stack.get()
        return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        size = self.queue_stack.qsize()
        result = None
        while size:
            result = self.queue_stack.get()
            self.queue_stack.put(result)
            size -= 1
        return result

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        size = self.queue_stack.qsize()
        return not size

if __name__ == '__main__':

    # Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    print(param_2, param_3, param_4)


