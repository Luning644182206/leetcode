class Solution:
    def numEnclaves(self, A):
        if not A:
            return 0

        one_place = []
        for i, item in enumerate(A):
            for j,num in enumerate(item):
                if num == 1:
                    one_place.append([j, i])
        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]
        x_len = len(A[0])
        y_len = len(A)
        res = 0
        for one in one_place:
            is_contain = []
            for i in range(4):
                is_contain_one = False # 默认没有被困住

                one_new = [one[0] + x[i], one[1] + y[i]]
                while 0 <= one_new[0] < x_len and 0 <= one_new[1] < y_len:
                    if one_new not in one_place:
                        is_contain_one = True
                        break
                    else:
                        one_new = [one_new[0] + x[i], one_new[1] + y[i]]

                is_contain.append(is_contain_one)

                if False in is_contain:
                    res += 1
                    break
        return len(one_place) - res


if __name__ == '__main__':
    a = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    b = Solution()
    print(b.numEnclaves(a))