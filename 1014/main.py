# coding=utf-8

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        weights_len = len(weights)
        min_len = int(weights_len/D) + int(weights_len%D)
        min_weights = 0
        days = 0

        # 循环第一次，找到参考值
        min_weights_arr = []
        counter = 0
        temp_min_weight = 0
        for item in weights:
            temp_min_weight += item
            if counter >= min_len-1:
                counter = 0
                min_weights_arr.append(temp_min_weight)
                temp_min_weight = 0
            else:
                counter += 1
        min_weights = max(min_weights_arr)

        # 开始寻找合理范围
        min_weights_arr = []
        temp_min_weight = 0
        while True:
            for index,item in enumerate(weights):
                if (temp_min_weight + item) < min_weights:
                    temp_min_weight += item
                else:
                    min_weights_arr.append(temp_min_weight)
                    temp_min_weight = item

            min_weights_arr.append(temp_min_weight)
            temp_min_weight = 0
            if len(min_weights_arr) <= D:
                if min_weights > max(min_weights_arr):
                    min_weights = max(min_weights_arr)
                    min_weights_arr = []
                else:
                    break
            else:
                break
        print(min_weights_arr)
        return min_weights


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    D = 5
    b = Solution()
    
    print(b.shipWithinDays(a,D))
    # a = [1,1,1,1,None]
    # print()