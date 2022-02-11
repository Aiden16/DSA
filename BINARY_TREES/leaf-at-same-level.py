class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        #Code here
        qu = deque([root])
        if not root:
            return True
        level = 0
        flag = 0
        while qu:
            for i in range(len(qu)):
                node = qu.popleft()
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
                if not node.left and not node.right:
                    flag = 1
            if flag:
                if not qu:
                    return True
                else:
                    return False
            level+=1
            