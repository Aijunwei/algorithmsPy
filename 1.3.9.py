# 输入缺少做括号的表达式，补齐左括号并输出
# 1 + 2 ) * 3 - 4) * 5 - 6 )))
# (( 1 + 2) * ((3 - 4) * (5 - 6)))
import re
def checkExpression():
    expression = input('请输入缺左括号的表达式：')
    print(f'输入表达式为：{expression}')
    # 存数据
    data = []
    # 存操作符合
    operator = []
    lastChar = None
    allOpt = ['+', '-', '*', '/']
    def combine():
        data2 = data.pop()
        data1 = data.pop()
        op = operator.pop()
        data.append(f'({data1} {op} {data2})')
    for char in expression:
        if char == ' ':
            continue
        elif re.match(r'\d', char):
            if lastChar and re.match(r'\d', lastChar):
                lastIndex = len(data) - 1
                data[lastIndex] = data[lastIndex] * 10 + int(char)
            else:
                data.append(int(char))
        elif char in allOpt:
            operator.append(char)
        elif char == ')':
            combine()
        lastChar = char
    while len(operator) > 0:
        combine()
    print(data.pop())


checkExpression()
