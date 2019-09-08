if __name__=='__main__':
    strings = input()
    string_contain = input()
    con_nums = int(input())
    con_arr = []
    for i in range(con_nums):
        lr = list(map(int, input().split(' ')))
        con_arr.append(lr)

    for item in con_arr:
        res = 0
        strings = list(strings)
        strings_split = strings[item[0]-1 : item[1]]
        strings_split = ''.join(strings_split)
        string_contain_len = len(list(string_contain))
        while string_contain in strings_split:
            res += 1
            if strings_split.find(string_contain) > -1:
                index = strings_split.find(string_contain)
                strings_split = list(strings_split)
                for i in range(string_contain_len):
                    del(strings_split[index])
                strings_split = ''.join(strings_split)
        
        
        print(res)

#     comeonmandontconconnect
# on
# 5
# 1 5
# 1 6
# 1 23
# 11 16
# 11 23