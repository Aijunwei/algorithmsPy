from typing  import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, item: T, next):
        super().__init__()
        self.item = item
        self.next = next

class Stack(Generic[T]):
    first = None
    n = 0
    def isEmpty(self):
        return self.first == None
    def size(self):
        return self.n
    def push(self, item: T):
        oldFirst = self.first
        self.first = Node(item, oldFirst)
        print('add', item, self.n)
        self.n += 1
    def pop(self):
        item = self.first.item
        self.first = self.first.next
        return item
    def peek(self):
        if self.n == 0:
            return None
        return self.first.item

def printStack(stack):
    first = stack.first
    while(first != None):
        print(first.item)
        first = first.next
if __name__ == '__main__':
    stack = Stack[int]()
    stack.push('1')
    stack.push('1')
    stack.push('1')
    stack.push('1')
    printStack(stack)
else:
    print('作为模块使用')
