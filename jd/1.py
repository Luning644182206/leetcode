
def max_deep(num_find, node_hash, deep):
    if num_find in node_hash.keys():
        deep += 1
        for item in 
        return max_deep(num_find, node_hash, deep)


if __name__ == '__main__':
    node_hash = {}
    node_num = int(input())
    node_lines = []
    for i in range(node_num-1):
        line = list(map(int, input().split(' ')))
        node_lines.append(line)

    for item in node_lines:
        if item[1] not in node_hash:
            node_hash[item[1]] = []
        node_hash[item[1]].append(item[0])

    max_deep = 0
    if len(node_hash.keys()) > 0:
        for item in node_hash[1]:
            max_deep(item, node_hash)



    else:
        print(0)
    
