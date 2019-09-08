# coding=utf-8

if __name__ == '__main__':
    all_string = []
    n = int(input())

    for i in range(n):
        all_string.append(input())

    for string in all_string:
        string_arr = list(string)
        new_string = []

        for item in string_arr:
            # 进栈操作
            new_string_len = len(new_string)
            is_push = True
            if new_string_len > 3:
                if item == new_string[-1] and new_string[-2] == new_string[-3]:
                    is_push = False

            if new_string_len > 2:
                if item == new_string[-1] and new_string[-2] == item:
                    is_push = False 

            if is_push:
                new_string.append(item)
        print(''.join(new_string))
