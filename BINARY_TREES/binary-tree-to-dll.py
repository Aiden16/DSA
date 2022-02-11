class Solution:
    def bToDLL(self,root):
        # do Code here
        #inplace recursive
        self.head = None
        self.to_return = None
        def inor(root):
            if not root:
                return
            inor(root.left)
            if not self.head:
                self.head = root
                self.to_return = root
            else:
                self.head.right = root
                root.left = self.head
                self.head = root
            
            # root.data
            inor(root.right)
        inor(root)
        return self.to_return
        
        #inplace iterative
        stck = []
        cur = root
        head = None
        to_return = None
        while True:
            if cur:
                stck.append(cur)
                cur = cur.left
            elif stck:
                node = stck.pop()
                if not head:
                    head = node
                    to_return = node
                else:
                    head.right = node
                    node.left = head
                    head = node
                cur = node.right
            else:
                break
        return to_return
        
                
        
        # #not in place
        arr = []
        def inorder(root):
            if not root:
                return
            left = inorder(root.left)
            arr.append(root.data)
            right = inorder(root.right)
        inorder(root)
        head = Node(arr[0])
        if len(arr) == 1:
            return head
        to_return = head
        for i in range(1,len(arr)-1):
            n = Node(arr[i])
            n.left = head
            head.right = n
            head = n
        tail = Node(arr[-1])
        tail.left = head
        head.right = tail
        # print(to_return.right.data)
        return to_return