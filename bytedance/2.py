# coding=utf-8

def finder(string_arr, pre, cur, maybe):
    # pre = 0
    # cur = 1
    len_string_arr = len(string_arr)
    # print(pre,cur)
    if pre >= len_string_arr or cur >= len_string_arr:
        return
    if string_arr[pre] == string_arr[cur]:
        if maybe:
            # 说明中了
            # right_cur = cur
            return cur
        else:
            maybe = True
            pre += 2
            cur += 2
            return finder(string_arr, pre, cur, maybe)
    else:
        maybe = False
        pre += 1
        cur += 1
        return finder(string_arr, pre, cur, maybe)

def finder_three(string_arr, pre, cur):
    len_string_arr = len(string_arr)
    # print(pre,cur)
    if pre >= len_string_arr or cur >= len_string_arr:
        return
    if string_arr[pre] == string_arr[cur]:
        cur_next = cur + 1
        if cur_next < len_string_arr:
            if string_arr[cur] == string_arr[cur_next]:
                return cur_next

    pre += 1
    cur += 1
    return finder_three(string_arr, pre, cur)




if __name__ == '__main__':
    all_string = []
    n = int(input())

    for i in range(n):
        all_string.append(input())

    for string in all_string:
        string_arr = []
        for item in string:
            string_arr.append(item)

        if len(string_arr) > 2:
            cur = 0
            while cur != None:
                cur = finder(string_arr, 0, 1, False)
                if cur != None:
                    del(string_arr[cur])

            cur = 0
            while cur != None:
                cur = finder_three(string_arr, 0, 1)
                if cur != None:
                    del(string_arr[cur])
        print(''.join(string_arr))