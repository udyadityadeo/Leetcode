class TreeNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class Solution:
    def hasCycle(self, head):
        if not head:
            return False
    
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasCycle(build_tree([3,2,0,-4])))
    print(sol.hasCycle(build_tree([1,2])))
