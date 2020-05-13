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
}

Base.readInut().then(data => {
    data = data.map(i => +i)
    console.log('输入的排序列', data) 
    QuickSort.sort(data, 0, data.length - 1)
    //QuickSort.partition(data, 0, data.length - 1)
    console.log('sorted', data)
})