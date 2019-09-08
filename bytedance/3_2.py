class Vertex:
    def __init__(self, key, val):
        self.id = key
        self.val = val
        self.connectedTo = {}

    #从这个顶点添加一个连接到另一个
    def addNeighbor(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight

    # def __str__(self):
    #     return str(self.id) + 'connectedTo' + str([x.id for x in self.connectedTo])

    #返回邻接表中的所有的项点
    def getConnections(self):
        return  self.connectedTo.keys()

    def getId(self):
        return self.id

    #返回从这个顶点到作为参数顶点的边的权重
    def getweight(self,nbr):
        return  self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key, val):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key, val)
        self.vertList[key] = newVertex
        return  newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return  self.vertList[n]
        else:
            return  None

    def __contains__(self, n):
        return  n in self.vertList

    def addEdge(self,f,t,const = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not  in self.vertList:
            nv = self.addVertex(t)
        # self.vertList[f].addNeighbor(self.vertList[t],const)
        self.vertList[f].addNeighbor(t,const)

    def getVertices(self):
        return  self.vertList.keys()

    def __iter__(self):
        return  iter(self.vertList.values())

if __name__ == '__main__':
    n = int(input()) # 有n个测试样例
    all_test = []

    for i in range(n):
        num = int(input())
        arr = list(map(int, input().split(' ')))
        all_test.append(arr)

    for arr in all_test:
        graph = Graph()

        # 增加点
        for index,item in enumerate(arr):
            graph.addVertex(index, item)

        # 增加边
        cur = 0
        while cur < len(arr):
            # print(cur)
            cur_next = cur + 1
            if cur_next < len(arr):
                if arr[cur_next] > arr[cur]:
                    graph.addEdge(cur_next, cur)
                elif arr[cur_next] < arr[cur]:
                    graph.addEdge(cur, cur_next)

            else:
                if arr[cur] > arr[0]:
                    graph.addEdge(cur, 0)
                elif arr[cur] < arr[0]:
                    graph.addEdge(0, cur)
            cur += 1

        # 拓扑排序
        vert_list = graph.vertList
        result = 0
        base_num = 1
        while True:
            empty_nodes = []
            for key in vert_list.keys():
                node = vert_list[key]
                # print('node', key, vert_list['1']['0'])
                if len(node.connectedTo.keys()) == 0:
                    empty_nodes.append(key)
                    result += base_num

            # base_num += 1
            if len(empty_nodes) > 0:
                for empty_node in empty_nodes:
                    for key in vert_list.keys():
                        node = vert_list[key]
                        if empty_node in node.connectedTo.keys():
                            # result += base_num
                            del vert_list[key].connectedTo[empty_node]

                    del vert_list[empty_node]
                base_num += 1
            else:
                break
        print(result)






















