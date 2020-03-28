# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        newList = None
        add = 0
        curNode = None
        while l1 or l2:
            num1 = 0
            num2 = 0
            if l1 != None:
                num1 = l1.val
                l1 = l1.next
            if l2 != None:
                num2 = l2.val
                l2 = l2.next
            sum = num1 + num2 + add
            if sum >= 10:
                node = ListNode(sum - 10)
                add = 1
            else:
                node = ListNode(sum)
                add = 0
            
            if newList == None:
                newList = node
                curNode = node
            else:
                curNode.next = node
                curNode = node
        if add == 1:
            curNode.next = ListNode(1)
        return newList


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
