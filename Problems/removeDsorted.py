class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        a = head
        while a and a.next:
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
        return head


#to build and print linked list for testing
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
    print(result)

if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 1, 2, 3, 3])
    result = sol.deleteDuplicates(head)
    print_linked_list(result)


    
