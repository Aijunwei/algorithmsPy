# 出列排序。说说你会如何将一副扑克牌排序（花色顺序是黑桃、红桃、梅花和方片），限制条件是只能查看最上面的两张牌，交换最上面的两张牌，或是将最上面的一张牌放到这摞牌的最下面。
# 不包含大小王
# 1-黑桃， 2-红桃 3-梅花 4-方片
# 参考冒泡法排序, 可以理解为选择排序的变形
from base import SortBase
class PokerSort(SortBase):
    def sort(self):
        data = self.data
        n = len(self.data)
        i = 0
        while i < n:
            j = 0
            while j < n:
                # 每次循环找到最大值，（n-1-i 之后的值是都是排过序的）
                if j < n-1-i and self.less(data[0], data[1]):
                    self.exch(0, 1)
                #elif j >= n-1-i and self.less(data[1], data[0]):
                #    self.exch(0, 1)
                data.append(data.pop(0))
                print(i, j, data)
                j += 1
            i += 1
        print('sorted:', data)
if __name__ == '__main__':
    data = [1,3,2,1,4,3,2,1,1,1,2,3,2,4,3,2,1]
    #data = [1,3,2,1,4,]
    print('扑克牌顺序🎴', data)
    PokerSort(data).sort()
                    
