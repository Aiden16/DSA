def LeftView(root):
    
    # code here
    if not root:
        return []
    qu = deque([root])
    left = []
    while qu:
        # print(qu[0].data)
        left.append(qu[0].data)
        for i in range(len(qu)):
            node = qu.popleft()
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)
    return left