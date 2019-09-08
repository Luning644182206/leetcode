# coding=utf-8
if __name__ == '__main__':
    n = int(input())
    coins = [64, 16, 4, 1] # 硬币
    counter = 0
    n = 1024 - n
    for item in coins:
        counter_temp = int(n/item)
        lost = int(n%item)
        counter += counter_temp
        n = lost
    print(counter)
