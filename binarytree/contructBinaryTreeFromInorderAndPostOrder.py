class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #       1
    #     /   \
    #    2     3
    #   / \   /  \
    #  4   5 6    7
    def __init__(self) -> None:
        pass
    
    # ROOT, LEFT, RIGHT
    def preOrder(self, root):
        st = []
        res = []
        st.append(root)
        while(len(st) > 0):
            node = st.pop()
            if node:
                res.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return res
    
    # LEFT, RIGHT, ROOT 
    # [4, 2, 5, 1, 6, 3, 7]
    def inOrder(self, root):
        curr = root
        st = []
        res = []
        while True:
            while curr:
                st.append(curr)
                curr = curr.left

            if (st):
                node = st.pop()
                res.append(node.val)
                curr = node.right
            
            if not st and not curr:
                break
            
        return res
    
    #LEFT, RIGHT, ROOT
    # PostOrder:  [4, 5, 2, 6, 7, 3, 1]
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
    
    
    def levelOrder(self, root):
        q = []
        r = []
        t = []
        
        if(root != None):
            pass
            
    
    #       1
    #     /   \
    #    2     3
    #   / \   /  \
    #  4   5 6    7
    # InOrder  :  [4, 2, 5, 1, 6, 3, 7] LEFT, ROOT, RIGHT
    # PostOrder:  [4, 5, 2, 6, 7, 3, 1] LEFT, RIGHT, ROOT
    def buildTree(self, inorder=None, postorder=None):
        print("Inorder: ", inorder) #Inorder --> LEFT, ROOT, RIGHT
        print("Postorder: ", postorder) #Postorder --> LEFT, RIGHT, ROOT
        self.index = len(postorder)
        hashMap = {n: i for i, n in enumerate(inorder)}
        
        def helper(l, r):
            if l > r:                   # checking l > r
                return None             # Return none if condition true
            self.index -= 1             # Reducing index 
            n = postorder[self.index]   # Starting from the root then right then left
            
            root = TreeNode(n)          # Creating Root node first then right then left
            
            i = hashMap[n]              # Getting the index value of nth node
            root.right = helper(i+1, r) # Setting the right node
            root.left = helper(l, i-1)  # Setting the left node
             
            return root                 # Finally returning root
        
        return helper(0, len(inorder)-1)
        
        
        
        


# In order traversal tree
inorder = [4, 2, 5, 1, 3]
postOrder = [4, 5, 2, 3, 1]

rootData = TreeNode(1)
rootData.left = TreeNode(2)
rootData.right = TreeNode(3)


rootData.left.left = TreeNode(4)
rootData.left.right = TreeNode(5)
rootData.right.left = TreeNode(6)
rootData.right.right = TreeNode(7)

print("PreOrder: ", Solution().preOrder(rootData))
print("InOrder: ", Solution().inOrder(rootData))
print("PostOrder: ", Solution().postOrder(rootData))