
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
}

module.exports = Base