# coding=-utf-8

class Solution(object):

    def findMin(self, weights, D, max_num, min_num):
        # 二分查找方法
        mid = int((max_num + min_num)/2)
        result = []
        temp_weights = 0
        for item in weights:
            if item + temp_weights < mid:
                temp_weights += item
            else:
                result.append(temp_weights)
                temp_weights = item
        result.append(temp_weights)
        temp_weights = 0
        if len(result) <= D:
            if max_num == mid:
                return mid
            max_num = mid
            mid = int((max_num + min_num)/2)
        else:
            min_num = mid
            print(max_num, min_num, len(result), D)
            mid = int((max_num + min_num)/2)
        # if min_num >= max_num:
        #     return min_num
        # print(min_num)
        return self.findMin(weights, D, max_num, min_num)


    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        min_num = max(weights)
        max_num = sum(weights)
        return self.findMin(weights, D, max_num, min_num)



if __name__=="__main__":
    a = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    b = Solution()
    
    print(b.shipWithinDays(a,D))
    # a = [1,1,1,1,None]
    # print()


