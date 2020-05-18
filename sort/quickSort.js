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
    //2.3.16
    static createBest(n) {
        let data = [];
        for(let i=0; i < n; i++) {
            data[i] = i;
        }
        
        QuickSort.best(data, 0, n-1);
        return data;
    }
    static best(data, lo, hi) {
        if (lo >= hi) {
            return
        }
        let mid = lo + Math.floor((hi - lo) / 2);
        QuickSort.best(data, lo, mid - 1);
        QuickSort.best(data, mid + 1, hi);
        Base.exch(data, lo, mid);
    }
    //2.3.17
    static partitionV2(data, lo, hi) {
        let i = lo;
        let j = hi + 1;
        const v = data[lo];
        while (true) {
            while (data[++i] < v);
            while (data[--j] > v);
            if (i >= j) break;
            QuickSort.exch(data, i, j);
        }
        QuickSort.exch(data, lo, j);
        return  j;
    }

    //2.3.17
    static sortV2(list, lo, hi) {
        if (lo >= hi) return
        QuickSort.printCurrent(list, lo, hi)
        //console.log('shuffle', list)
        let dividerIndex = QuickSort.partitionV2(list, lo, hi);
        console.log('dividerIndex=', dividerIndex, list, )
        let leftHi;
        //保证左子树最右侧为最大值，可以去除partition右侧边界检查
        if (dividerIndex == hi) {//切分位置为hi，会无限递归
            leftHi = dividerIndex - 1;
            Base.exch(list, lo, leftHi)
        } else if ((dividerIndex - lo) <= 2) {
            leftHi = dividerIndex - 1;
        }
        else {
            leftHi = dividerIndex
        }
        QuickSort.sortV2(list, lo, leftHi)
        QuickSort.sortV2(list, dividerIndex + 1, hi)
    }
    static printCurrent(list, lo, hi) {
        let cur = []
        for (let i = lo; i<=hi; i++) {
            cur.push(list[i])
        }
        console.log(cur, lo, hi)
    }
    static partitionV3(list, lo, hi, stack) {
        const v = list[lo];
        let i = lo;
        let j = hi + 1;
        while(true) {
            while (list[++i] < v) {
                if (i == hi) break;
            }
            while (list[--j] > v);
            if (i >= j) break;
            Base.exch(list, i, j)
        }
        Base.exch(list, j, lo)
        if (j < hi) { // push right child
            stack.push(list.slice(j + 1))
        }
        stack.push(v);
        if (j > lo) { //push left child
            stack.push(list.slice(lo, j))
        }
        console.log('stack', stack);
    }
    static quickSortv3(list, lo, hi) {
        const stack = [];
        const output = [];
        QuickSort.partitionV3(list, lo, hi, stack);
        while (stack.length) {
            let item = stack.pop();
            if (Array.isArray(item)) {
                let len = item.length;
                if (len == 1) {
                    output.push(item[0]);
                } else {
                    QuickSort.partitionV3(item, lo, len - 1, stack)
                }
            } else {
                output.push(item)
            }
        }
        console.log('sorted', output)

    }
}
/*
Base.readInut().then(data => {
    data = data.map(i => +i)
    Base.shuffle(data)
    console.log('shuffle:', data) 
    //QuickSort.sort(data, 0, data.length - 1)
    //QuickSort.partition(data, 0, data.length - 1)
    QuickSort.threeDividerSort(data, 0, data.length - 1)
    console.log('sorted', data)

})*/

//2.3.16
//console.log('best sorted', QuickSort.createBest(10))
//2.3.17
/*
Base.readInut().then(data => {
    data = data.map(i => +i)
    Base.shuffle(data, 0, data.length - 1);
    console.log('shuffle', data)
    //QuickSort.sortV2(data, 0, data.length - 1)
    
    QuickSort.sortV2(data, 0 , data.length-1)
    console.log('sorted', data)
})*/

Base.readInut().then(data => {
    data = data.map(i => +i)
    Base.shuffle(data, 0, data.length - 1);
    console.log('shuffle', data)
    //QuickSort.sortV2(data, 0, data.length - 1)
    
    QuickSort.quickSortv3(data, 0 , data.length-1)
})