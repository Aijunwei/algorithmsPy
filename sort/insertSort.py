# 插入排序

from base import SortBase

class InsertSort(SortBase):
    def moveRight(self, i, j):
        data = self.data
        t = data[i]
        while i > j + 1:
            data[i] = data[i - 1]
            i -= 1
        data[i] = t
    def sort(self):
        data = self.data
        n = len(data)
        if n > 1:
            i = 1
            while i < n:
                j = i - 1
                while j >= 0:
                    if self.less(data[i], data[j]):
                        break
                    j -= 1
                self.moveRight(i, j)
                i += 1
        print('排序后：', self.data)

if __name__ == '__main__':
    inputStr = input('请输入待排序元素(3 4 5 1 6)：')
    data = inputStr.split()
    InsertSort(data).sort()