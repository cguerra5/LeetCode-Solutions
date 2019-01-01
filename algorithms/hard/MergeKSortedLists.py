import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def popListNode(self, min_heap, lists):
        """
        Pops an item from a min heap where each element in the heap is of form
        (idx, lists[idx]) and returns its value lists[idx].val as a ListNode.
        This will also remove the first node from list[idx] and replace it with
        the second node, if it exists.
        
        :type min_heap: List[(int, int)]
        :type lists: List[ListNode]
        :rtype ListNode
        """
        val, idx = heapq.heappop(min_heap)
        # Since the original head of lists[idx] was popped off the min_heap,
        # remove the head from the original lists array
        lists[idx] = lists[idx].next
        if lists[idx] != None:
            heapq.heappush(min_heap, (lists[idx].val, idx))
        return ListNode(val)

        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        # Create a min heap of elements (head, list_index), where head is the
        # first node in lists[list_index] and the smallest head is at the top
        # of the min heap.
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
        
        if not min_heap:
            return []
        
        merged_list = self.popListNode(min_heap, lists)
        next_node = merged_list
        while len(min_heap) > 0:
            next_node.next = self.popListNode(min_heap, lists)
            next_node = next_node.next
        
        return merged_list

arr_lists = [[1, 3, 4], [2, 6], [1, 4, 5]]
ListNode_lists = []
for arr in arr_lists:
    head = ListNode(arr[0])
    next_node = head
    for elt in arr[1:]:
        next_node.next = ListNode(elt)
        next_node = next_node.next
    ListNode_lists.append(head)

s = Solution()
s.mergeKLists([[]])

