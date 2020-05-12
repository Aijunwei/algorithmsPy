const Base = require('./base.js');

class MergeSort {
    static merge(list, aux, lo, mid, hi) {
        let i = lo;
        let j = mid + 1;
        for(let k=lo; k <= hi; k++) {
            aux[k] = list[k]
        }
        for (let k=lo; k <= hi; k++) {
            if (i > mid) {
                list[k] = aux[j++];
            } else if (j > hi) {
                list[k] = aux[i++];
            } else if (Base.less(aux[i], aux[j])) {
                list[k] = aux[i++]
            } else {
                list[k] = aux[j++]
            }
        }
    }

    static sort(list) {
        const aux = list.slice(0);
        const N = list.length;
        for(let sz=1; sz < N; sz=sz*2) {
            for(let lo = 0; lo < N-sz; lo = lo + sz * 2) {
                MergeSort.merge(list, aux, lo, lo+sz-1, Math.min(N - 1, lo + sz * 2 - 1))
            }
        }
        console.log('sorted', list)
    }
}

Base.readInut().then(list => {
    console.log(list);
    MergeSort.sort(list)
})

