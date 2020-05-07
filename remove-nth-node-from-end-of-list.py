#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        cachelist = []
        first = head
        while head is not None:
            item = head
            head = head.next
            cachelist.append(item)
        cachelistLen = len(cachelist)
        if n == cachelistLen:
            newHead = first.next
            first.next = None
        elif n == 1:
            newHead = first
            cachelist[cachelistLen - 2].next = None
        else:
            delIndex = cachelistLen - n
            delItem = cachelist[delIndex]
            preItem = cachelist[delIndex -1]
            nextItem = cachelist[delIndex + 1]
            preItem.next = nextItem
            delItem.next = None
            newHead = first
        return newHead
    # 双指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy =  ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        i = 1
        while i <= n+1:
            first = first.next
            i += 1
        
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

def generateList(n: int):
    head = ListNode(n)
    cacheHead = head
    n = n - 1
    while n > 0:
        newNode = ListNode(n)
        head.next = newNode
        head = newNode
        n = n - 1
    return cacheHead

def printList(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next
initList = generateList(10)
#printList(initList)
printList(Solution().removeNthFromEnd(initList, 10))