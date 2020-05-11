# 插入排序

from base import SortBase

class ShellSort(SortBase):
    def moveRight(self, i, j, step):
        data = self.data
        t = data[i]
        while i > j + step:
            data[i] = data[i - step]
            i -= step
        data[i] = t
    def sort(self):
        steps = [1]
        data = self.data
        n = len(data)
        step = 1
        stepLimit = n // 3
        while step < stepLimit:
            step = 3 * step + 1
            steps.append(step)
        print('maxStep=', step, steps)

        if n > 1:
            #while step >= 1:
            while len(steps) > 0:
                step = steps.pop()
                i = step
                while i < n:
                    j = i - step
                    while j >= 0:
                        if self.less(data[i], data[j]):
                            break
                        j -= step
                    self.moveRight(i, j, step)
                    i += 1
                print(f'step:{step}排序：', self.data)
                # step = step // 3
        print('排序后：', self.data)

if __name__ == '__main__':
    inputStr = input('请输入待排序元素(3 4 5 1 6)：')
    data = inputStr.split()
    ShellSort(data).sort()