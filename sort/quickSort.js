const Base = require('./base.js');

class QuickSort {
    static sort(list, lo, hi) {
        if (lo >= hi) return
        let dividerIndex = QuickSort.partition(list, lo, hi);
        QuickSort.sort(list, lo, dividerIndex-1)
        QuickSort.sort(list, dividerIndex + 1, hi)
    }
    static partition(list, lo, hi) {
        let i = lo;
        let j = hi + 1;
        const v = list[lo];
        
        while (true) {
            while (list[++i] < v) {
                //console.log('i=', i)
                if (i == hi) break;
            }
            while (list[--j] > v) {
                if (j == lo) break;
            }
            if (i >= j) break;
            QuickSort.exch(list, i, j)
        }
        QuickSort.exch(list, lo, j)
        return  j
    }
    static exch(list, i, j) {
        let tmp = list[i];
        list[i] = list[j];
        list[j] = tmp;
        /**
         * 不依赖tmp交换1
         * list[i] = list[i] - list[j]
         * list[j] = list[i] + list[j]
         * list[i] = list[j] - list[i]
         */
        /**
         * 不依赖tmp交换2
         * list[i] = list[i]^list[j]
         * list[j] = list[i]^list[j]
         * list[i] = list[i]^list[j]
         */
    }
    /**
     * 三向切分快速排序
     * 对于有大量重复的数据快速排序可能使得排序时间从线性对数级别降级到平方级别
     * 先对数据进行一次整理
     * v-比较基准，lt指针 a[lo..lt] 小于v，gt指针：a[gt+1..hi]大于v；a[lt+1, gt] 等于v
     * a[i] 小于 v,把a[lt]和a[i]互换，lt和i加一
     * a[i]大于v，把a[gt]和a[i]互换，gt减一
     * a[i]等于v，则i加一
     */
    static threeDividerSort(data, lo, hi) {
        let lt = lo;
        let i = lo + 1;
        let gt = hi;
        const v = data[lo];
        while (i <= gt) {
            if (data[i] < v) {
                QuickSort.exch(data, i, lt);
                i++;
                lt++;
            } else if (data[i] > v) {
                QuickSort.exch(data, i, gt)
                gt--;
            } else {
                i++;
            }
            //此时data[lo..lt] <=data[lt+1..gt-1] <=data[gt+1..hi],再对左右边使用快速排序
            QuickSort.sort(data,lo,lt);
            QuickSort.sort(data, gt+1, hi)
        }
    }
}

Base.readInut().then(data => {
    data = data.map(i => +i)
    Base.shuffle(data)
    console.log('shuffle:', data) 
    //QuickSort.sort(data, 0, data.length - 1)
    //QuickSort.partition(data, 0, data.length - 1)
    QuickSort.threeDividerSort(data, 0, data.length - 1)
    console.log('sorted', data)
})