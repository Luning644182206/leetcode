if __name__ == '__main__':
    n = int(input())
    n_list = []
    counter = 0
    result = []
    for i in range(n):
        counter += 1
        n_list.append(counter)
    
    while len(n_list) > 0:
        num = n_list[0]
        result.append(num)
        n_list.pop(0)
        print(num, end=" ")

        if len(n_list) > 0:
            num = n_list[0]
            n_list.pop(0)
            n_list.append(num)