# coding=utf-8
        
if __name__ == '__main__':
    n = int(input()) # 有个测试样例
    all_test = []

    for i in range(n):
        # all_test.append(map(int, input().split(' ')))
        num = int(input())
        arr_string = input()
        arr_string = arr_string.split(' ')
        arr = []
        pre_val = None
        next_val = None
        for item in range(num):
            node = Node(int(arr_string[item]))
            node.pre = pre_val
            pre_val = node.val
            arr.append(node)
        arr[0].pre = arr[num-1].val

        for item in range(num):
            if item+1 < num:
                arr[item].next = arr[item+1].val
        all_test.append(arr)

    for arr in all_test:
        result = 0
        for item in arr:

        print()
    