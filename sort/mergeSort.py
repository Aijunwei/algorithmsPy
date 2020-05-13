# 归并排序

from base import SortBase

class MergeSort(SortBase):
    tmp = []
    def __init__(self, data):
        super().__init__(data)
        for i in data:
            self.tmp.append(i)
    def merge(self, lo, mid, hi, di):
        i,j = lo, mid+1
        k = lo

        #while k <= hi:
        #    self.tmp[k] = self.data[k]
        #    k += 1
        #k = lo
        if di == 0:
            left = self.data
            right = self.tmp
        else:
            left = self.tmp
            right = self.data
        while k<=hi:
            if lo == 7 and hi == 10:
                print(i, j)
            if i > mid:
                #self.data[k] = self.tmp[j]
                left[k] = right[j]
                j += 1
            elif j > hi:
                #self.data[k] = self.tmp[i]
                left[k] = right[i]
                i += 1
            #elif self.less(self.tmp[i], self.tmp[j]):
            elif self.less(right[i], right[j]):
                #self.data[k] = self.tmp[j]
                left[k] = right[j]
                j += 1
            else:
                #self.data[k] = self.tmp[i]
                left[k] = right[i]
                i += 1
            k += 1
    def sort(self, lo, hi, di):
        if lo >= hi:
            return
        nextDi = di ^ 1 #异或 用于控制排序方向
        mid = lo + (hi - lo) // 2
        self.sort(lo, mid, nextDi)
        self.sort(mid + 1, hi, nextDi)

        if di == 0:
            right = self.tmp
        else:
            right = self.data
        #if int(self.data[mid]) <= int(self.data[mid + 1]):
        if int(right[mid]) <= int(right[mid + 1]):
            return
        self.merge(lo, mid, hi, di)


if __name__ == '__main__':
    inputStr = input('请输入待排序元素：')
    data = inputStr.split()
    hi = len(data) - 1
    mid = hi // 2
    MergeSort(data).sort(0, hi, 0)
    print('sorted', data)
    