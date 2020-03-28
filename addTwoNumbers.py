# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        curNode = newList = ListNode(0)
        sum = 0
        while l1 or l2 or sum != 0:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            node = ListNode(sum % 10)
            sum //= 10
            curNode.next = node
            curNode = node
        return newList.next


def createList(li):
    head = None
    curNode = None
    #reverseList = list(reversed(li))
    #print(reverseList)
    for i in li:
        node = ListNode(i)
        if curNode:
            curNode.next = node
            curNode = node
        else:
            curNode = head = node
    return head

def printList(list):
    str = ''
    while list:
        str += f'{list.val} ->'
        list = list.next
    print(str)
l1 = createList([9,8])
l2 = createList([1])
printList(l1)
printList(l2)
printList(Solution().addTwoNumbers(l1, l2))
