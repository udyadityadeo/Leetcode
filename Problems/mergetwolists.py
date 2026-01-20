from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergetwolists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def build_linked_list(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(" -> ".join(map(str, result)))

if __name__ == "__main__":
    sol = Solution()
    list1 = build_linked_list([1,2,4])
    list2 = build_linked_list([1,3,4])
    merged_list = sol.mergetwolists(list1, list2)
    print_linked_list(merged_list)

