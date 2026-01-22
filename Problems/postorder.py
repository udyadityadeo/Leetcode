def postorder(self, root):
    stack = []
    res = []
    curr = root
    last_visited = None

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
            curr = stack[-1]

        if curr.right and curr.right != last_visited:
            curr = curr.right
        else:
            res.append(curr.val)
            last_visited = stack.pop()

    return res