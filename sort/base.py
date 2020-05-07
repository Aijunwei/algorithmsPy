# 基础类

class SortBase:
    data = []
    def __init__(self, data):
        super().__init__()
        self.data = data
        print('init data=', data)
    def less(self, a, b):
        return int(b) - int(a) < 0
    def exch(self, i, j):
        data = self.data
        t = data[i]
        data[i] = data[j]
        data[j] = t