# coding=-utf8

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        change_num = 0
        num_arr = {
            'A': [0,0,0,0,0,0,0],
            'B': [0,0,0,0,0,0,0]
        }
        for item in A:
            num_arr['A'][item] += 1
        for item in B:
            num_arr['B'][item] += 1
        max_num_A = max(num_arr['A'])
        max_num_B = max(num_arr['B'])
        target_arr = []
        source_arr = []
        max_index = 0
        max_num = 0
        if max_num_A >= max_num_B:
            target_arr = A
            source_arr = B
            max_index = num_arr['A'].index(max_num_A)
            max_num = max_num_A
        else:
            target_arr = B
            source_arr = A
            max_index = num_arr['B'].index(max_num_B)
            max_num = max_num_B



        # for item in A:
        #     num_arr[item] += 1
        # max_num = max(num_arr)
        if max_num != len(target_arr):
            for index,item in enumerate(source_arr):
                if item == max_index:
                    if target_arr[index] != max_index:
                        change_num += 1
            if change_num != (len(target_arr)-max_num):
                change_num = -1

        return change_num

           
if __name__ == '__main__':
    

    A = [1,2,1,1,1,2,2,2]
    B = [2,1,2,2,2,2,2,2]
    b = Solution()
    
    print(b.minDominoRotations(A, B))

