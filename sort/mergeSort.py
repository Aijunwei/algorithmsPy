# 插入排序

from base import SortBase

class MergeSort(SortBase):
    tmp = []
    def __init__(self, data):
        super().__init__(data)
        for i in data:
            self.tmp.append(i)
    def merge(self, lo, mid, hi):
        i,j = lo, mid+1
        k = lo
        while k <= hi:
            self.tmp[k] = self.data[k]
            k += 1
        k = lo
        while k<=hi:
            if i > mid:
                self.data[k] = self.tmp[j]
                j += 1
            elif j > hi:
                self.data[k] = self.tmp[i]
                i += 1
            elif self.less(self.tmp[i], self.tmp[j]):
                self.data[k] = self.tmp[j]
                j += 1
            else:
                self.data[k] = self.tmp[i]
                i += 1
            k += 1
    
    def sort(self, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self.sort(lo, mid)
        self.sort(mid + 1, hi)
        if int(self.data[mid]) <= int(self.data[mid + 1]):
            return
        self.merge(lo, mid, hi)

if __name__ == '__main__':
    inputStr = input('请输入待排序元素：')
    data = inputStr.split()
    hi = len(data) - 1
    mid = hi // 2
    MergeSort(data).sort(0, hi)
    print('sorted', data)
    