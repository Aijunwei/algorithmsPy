# 动态联通性
class WeightQuickUnionUF:
    def __init__(self, n: int):
        super().__init__()
        self.n = n
        self.id = []
        self.sz = []
        self.count = n
        self.treeData = {}
        for i in range(n):
            self.id.append(i)
            self.sz.append(1)
            # self.treeData[i] = [i,]
            print(self.id, self.sz)
    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)
    def find(self, p: int):
        # 找到根节点
        route = []
        while p != self.id[p]:
            route.append(p)
            p = self.id[p]
        for i in route:
            # self.treeData.pop(i)
            self.id[i] = p
        return p
    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        print('i,j=', i, j)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.updateSubItem(i, j)
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.updateSubItem(j, i)
            self.sz[i] += self.sz[j]
        self.count = self.count - 1
    def updateSubItem(self, pre, next):
        for index, i in enumerate(self.id):
            if i == pre:
                self.id[index] = next
    def transformData(self):
        treeData = {}
        for index, i in enumerate(self.id):
            print('index,i', index, i)
            if i == index:
                if treeData.get(index, None) == None:
                    treeData[index] = [i]
            else:
                if treeData.get(i, None) == None :
                    treeData[i] = [index]
                else:
                    treeData[i].append(index)
                    
        return treeData
    def drawTree(self):
        tree = self.transformData()
        #tree =  {6: [0, 1, 2, 5, 7, 8], 4: [3, 8, 9], 2: [1,4]}
        print('draw tree:', tree)
        for key in tree:
            item = tree[key]
            strItem = list(map(lambda x: str(x), item))
            length = len(item)
            half = length // 2
            ifOdd = length % 2 == 1
            #print('ifOdd', ifOdd)
            print(str(key).center(length * 2 + 1))
            if ifOdd:
                trunk1 = ("/"*half).rjust(length)+ '|' + ("\\"*half).ljust(length)
                trunk2 = ('/'*half).rjust(length-1)+ ' | ' + ('\\'*half).ljust(length)
                if length == 1:
                    leaf = f' {strItem[0]} '
                else:
                    leaf = "".join(strItem[0:half]).rjust(length - 2) + f'  {strItem[half]}  ' + "".join(strItem[(half + 1):]).ljust(length)
            else:
                trunk1 = ('/'*half).rjust(length)+ ' ' + ('\\'*half).ljust(length)
                trunk2 = ('/'*half).rjust(length - 1)+ '   ' + ("\\"*half).ljust(length)
                if length == 2:
                    leaf = f'{strItem[0]}   {strItem[1]}'
                else:
                    leaf = "".join(strItem[0:half]).rjust(length - 2) + f'     ' + "".join(strItem[(half):]).ljust(length)
            print(trunk1)
            print(trunk2)
            print(leaf)
            print()


if __name__ == '__main__':
    uf  = WeightQuickUnionUF(10)
    uf.drawTree()
    while True:
        inputParam = input('请输入整数对0-9（例如：1,3）')
        if inputParam == '':
            break
        pq = inputParam.split(',')
        p, q = int(pq[0]), int(pq[1])
        # print(f'p,q={p},{q}')
        
        if uf.connected(p, q):
            print(uf.id)
            uf.drawTree()
            continue
        uf.union(p, q)
        print(uf.id)
        print(f'{p} {q}')
        uf.drawTree()
    print(f'有{uf.count}个通量')