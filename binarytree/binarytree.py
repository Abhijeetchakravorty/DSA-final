class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass
    
    def preOrder(self, root):
        st, res = [], []
        if (root == None):
            return root
        st.append(root)
        while(len(st) > 0):
            node = st.pop()
            if (node):
                res.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return res
    
    def inOrder(self, root):
        curr = root
        st = []
        res = []
        while(True):
            while(curr):
                st.append(curr.val)
                curr = curr.left
            
            if st:
                node = st.pop()
                res.append(node.val)
                curr = curr.right
                
            if not st and not curr:
                break
        
        return res
    
    def postOrder(self, root):
        traversal, st = [], [(root, False)]
        while(len(st) > 0):
            node, visited = st.pop()
            if node:
                if visited:
                    traversal.append(node.val)
                else:
                    st.append((node, True))
                    st.append((node.right, False))
                    st.append((node.left, False))
        return traversal
    
    def levelOrderTraversal(self, root):
        q = []
        r = []
        t = []
        if(root != None):
            q.append(root)
            q.append("X")
        
        while(len(q) > 0):
            head = q.pop(0)
            if (head == "X"):
                r.append(t)
                if(len(q) > 0):
                    q.append("X")
                    t = []
            else:
                t.append(head.val)
                if(head.left):
                    q.append(head.left)
                if(head.right):
                    q.append(head.right)
        return r