# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    while head.next != None:
        print('{}->'.format(head.val), end='')
        head = head.next
    print(head.val)

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        # Get the k-th node in the linked list
        i = 0
        kth_node = head
        while kth_node != None and i < k:
            kth_node = kth_node.next
            i += 1
        
        if i < k:
            return head
        
        next_node = kth_node:
        while next_node != None:
            i += 1
        list_len = i
        
        i = 0
        original_head = head
        next_head = head.next
        while head != None and i < k:
            head.next = kth_node
            if i != k - 1:
                kth_node = head
                head = next_head
                if next_head:
                    next_head = next_head.next
            i += 1
        
        return head

head = ListNode(0)
prev_node = head
for i in range(1, 20):
    new_node = ListNode(i)
    prev_node.next = new_node
    prev_node = new_node

k = 10

s = Solution()
printList(s.reverseKGroup(head, k))

