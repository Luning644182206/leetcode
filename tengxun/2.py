if __name__ == '__main__':
    use_m = [] #f1
    unuse_m = [] #f2
    arr = []
    n = int(input())
    n_num = n
    while n:
        arr.append(int(input()))
        n -= 1
        use_m.append(0)
        unuse_m.append(0)

    # use_m.append(0)
    # unuse_m.append(0)
    # arr.append
    for i in range(n_num):
        # item = i + 1
        # print(i)
        use_m[i] = min([unuse_m[i-1], use_m[i - 1]]) + arr[i]
        unuse_m[i] = min([use_m[i-1], use_m[i - 2]])
    
    # print(unuse_m)
    # print(use_m)

    result = min([use_m[n-1], unuse_m[n-1]])
    print(result)
