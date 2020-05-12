
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
}

module.exports = Base