def reverseLevelOrder(root):
    # code here
    ans = []
    qu = deque([root])
    while qu:
        for i in range(len(qu)):
            node = qu.popleft()
            ans.append(node.data)
            if node.right:
                qu.append(node.right)
            if node.left:
                qu.append(node.left)
    ans.reverse()
    return ans