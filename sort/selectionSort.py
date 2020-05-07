# 选择排序
from base import SortBase

class SelectionSort(SortBase):
    def __init__(self, data):
        super().__init__(data)
    def sort(self):
        data = self.data
        n = len(self.data)
        i = 0
        while i < n:
            j = i + 1
            min = i
            while j < n:
                if self.less(data[min], data[j]):
                    min = j
                j += 1
            self.exch(i, min)
            i += 1

        print('sorted:', data)

if __name__ == '__main__':
    inputStr = input('请输入待排序元素(3 4 5 1 6)：')
    data = inputStr.split()
    SelectionSort(data).sort()