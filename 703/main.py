import queue 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.priority_queue = queue.PriorityQueue()
        for item in nums:
            self.add(item)

    def add(self, val: int) -> int:
        size = self.priority_queue.qszie()
        if size < self.k:
            self.priority_queue.put(val)
        else:
            small = self.priority_queue.get()
            if val > small:
                self.priority_queue.put(val)
            else:
                self.priority_queue.put(small)

        small = self.priority_queue.get()
        self.priority_queue.put(small)
        return small


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__=="__main__":
    priority_queue = queue.PriorityQueue()
    priority_queue.put(1)
    priority_queue.put(2)
    print (priority_queue.get())