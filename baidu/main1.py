# if __name__ == '__main__':
#     _dic = {}

#     strings = input()
#     strings_arr = list(strings)

#     for i in range(len(strings_arr)):
#         char_one = strings_arr[0]
#         del(strings_arr[0])
#         strings_arr.append(char_one)
#         strings_arr = ''.join(strings_arr)

#         if strings_arr not in _dic:
#             _dic[strings_arr] = 1
#         strings_arr = list(strings_arr)

#     print(len(_dic.keys()))


if __name__ == '__main__':
    _dic = {}

    strings = input()

    for i in range(len(strings)):
        strings = strings[1:] + strings[0]
        if strings not in _dic:
            _dic[strings] = 1

    print(len(_dic.keys()))






