if __name__ == '__main__':
    n, a = map(int, input().split())
    # n = 3
    # a = 10
    arr = []
    for i in range(n):
        arr.append(int(input()))

    end = arr[-1]
    start = arr[0]

    end_cha = end - a
    start_cha = a - start

    result = 0
    if end_cha > start_cha:
        result = arr[-2] - arr[0] + start_cha
    else:
        result = arr[-1] - arr[1] + end_cha
    print(result)
