# 编写一个Stack的用例Parenthess， 从标准输入读取一个文本流并使用栈判断括号是否匹配完整，例如[()]{}{[()()]()}程序打印true
# 对于[(]打印false
#from stack import Stack, printStack
# import re

def checkBrackets(left, right) -> bool:
    return (left == '[' and right == ']') or (left == '{' and right == '}') or (left == '(' and right == ')')
    
def check():
    str = input('请输入：')
    print(f'输入的字符串是：{str}')
    stack = []   
    for letter in str:
        stackLen = len(stack)
        if letter not in ['[', ']', '{', '}', '(', ')']:
            continue
        if stackLen == 0:
            stack.append(letter)
        elif checkBrackets(stack[stackLen - 1], letter):
            stack.pop()
        else:
            stack.append(letter)
    if len(stack) > 0:
        print('false')
    else:
        print('true')

check()
