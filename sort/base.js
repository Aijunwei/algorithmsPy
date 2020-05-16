
class Base {
    static less(a, b) {
        return a - b < 0
    }

    static readInut() {
        return new Promise(resolve => {
            const readline = require('readline');
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            })
            rl.question('请输入待排序的数据，以空格隔开（例如：1 4 3 2）：', data => {
                //console.log('输入的数据是', data)
                resolve(data.split(' '))
                rl.close()
            })
        })
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
     * 原来，在Chrome v8引擎源码中，处理sort方法时，使用了插入排序和快速排序两种方案。当目标数组长度小于10时，使用插入排序；反之，使用快速排序和插入排序的混合排序。
     * 所以用 sort 方法乱序不准确的原因就在于：理想的方案是数组中每两个元素都要进行比较，这个比较有50%的交换位置概率。而在插入排序的算法中，当待排序元素跟有序元素进行比较时，一旦确定了位置，就不会再跟位置前面的有序元素进行比较，所以就乱序的不彻底
     * 链接：https://www.jianshu.com/p/ce5b606b507d
     */
    static pseudoShuffle(data) {
        return data.sort(() => Math.random() - 0.5)
    }
    /**
     * 1. 从数组最后一个开始循环i=len - 1
     * 2. 每次从0 -（i-1）之间随机抽取一个数与 i  交换，此时i位置的数是随机放置的数
     * 3. 直到i=0 结束
     * @param {array} data 
     */
    static shuffle(data) {
        let i = data.length
        while(i) {
            let rand = Math.floor(Math.random() * i--);
            [data[i], data[rand]] = [data[rand], data[i]]
        }
    }
}

module.exports = Base