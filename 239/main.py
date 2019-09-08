# coding=utf-8
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        result = []
        window = []

        for index,item in enumerate(nums):
            # 如果这个窗口已经开移动了
            # 那就把在这个窗口前的数值都抛掉
            if index >= k and window[0] <= index-k:
                del(window[0])

            # 保持最大的一直在第一个
            # 只要有大的进来，就把小的都抛掉
            while window and nums[window[-1]] <= item:
                window.pop()

            # 把本次数据加进来
            window.append(index)

            # 符合窗口了，就开始输出数值
            if index >= k-1:
                result.append(nums[window[0]])
        return result


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__=="__main__":
    a = Solution()
    print(a.maxSlidingWindow([1, -1], 1))