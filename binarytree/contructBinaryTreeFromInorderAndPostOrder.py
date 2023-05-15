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
        st = [] # created new stack
        res = [] # Created result array
        st.append(root) #adding elements to the stack
        while(len(st) > 0): # iterating  each element
            node = st.pop() # popping element
            if node: 
                res.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return res
    
    def buildTree(self, nodeType, node):
        strData = ""
        if(nodeType=="left"):
            strData = """/
                        """+node.val
        elif(nodeType=="right"):
            strData = """\
                        """+node.val
        return strData
    
    def visualizePreOrder(self, root, n):
        # print(root)
        # node = ""
        # nodeData = """ 
        #         ---
        #         | |
        #         ---
        #     """
        st = []
        res = []
        st.append(root)
        while(len(st) > 0):
            node = st.pop()
            if(node):
                print(node.val, "\n")
                res.append(node.val)
                st.append(node.right)
                st.append(node.left)
        return res
    
    # LEFT, ROOT, RIGHT 
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

    def levelOrder(self, root):
        q = []
        r = []
        t = []
        
        if(root != None):
            q.append(root)
            q.append("X")
        
        while(len(q) > 0):
            head = q.pop(0)
            if(head == "X"):
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

    def maxDepth(self, root):
        if not root:
            return 0
        
        max_depth = 0
        def dfs(node, depth):
            nonlocal max_depth
            
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
            
            if node.left:
                dfs(node.left, depth+1)
            
            if node.right:
                dfs(node.right, depth+1)
        
        dfs(root, 1)
        return max_depth
    
    def isSame(self, p, q):
        if p and q:
            return (p.val==q.val and self.isSame(p.left, q.right) and self.isSame(p.right, q.left))
        return p is q
    
    def isSymmetric(self, root):
        if root:
            return self.isSame(root.left, root.right)
        else:
            return False
    
    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
    
    # Construct Binary Tree from Inorder and Postorder Traversal
    #       1
    #     /   \
    #    2     3
    #   / \   /  \
    #  4   5 6    7
    # InOrder  :  [4, 2, 5, 1, 6, 3, 7] LEFT, ROOT, RIGHT
    # PostOrder:  [4, 5, 2, 6, 7, 3, 1] LEFT, RIGHT, ROOT
    def buildTree(self, inorder=None, postorder=None):
        # print("Inorder: ", inorder) #Inorder --> LEFT, ROOT, RIGHT
        # print("Postorder: ", postorder) #Postorder --> LEFT, RIGHT, ROOT
        self.index = len(postorder) 
        hashMap = {n: i for i, n in enumerate(inorder)}
        print("hashMap: ", hashMap)
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
        
    # Construct Binary Tree from Inorder and Postorder Traversal
    # def buildTree(self, inorder, postorder):
    #     # build a map of inorder array {value: index} for easy look-up
    #     inorder_index = {}
    #     self.index = 1
    #     for i, val in enumerate(inorder):
    #         inorder_index[val] = i

    #     # left and right is the pointer for inorder, post is the index of root val in postorder
    #     def arrayToTree(left, right):

    #         # edge case
    #         if left > right:
    #             return None
        
    #         # use postorder[-1] as root, and get its index from hashtable
    #         root_val = postorder[-self.index]
    #         root = TreeNode(root_val)
    #         self.index += 1

    #         # root.right = buildtree(right_inorder, right_postorder)
    #         # do the right child first because in post order, before root it the right child
    #         root.right = arrayToTree(inorder_index[root_val] + 1, right)

    #         # root.left = buildtree(left_inorder, left_postorder)
    #         root.left = arrayToTree(left, inorder_index[root_val] - 1)

    #         return root

    #     return arrayToTree(0, len(inorder) - 1)

    #build tree from preorder and inorder traversal
    # preorder: ROOT, LEFT, RIGHT
    # inorder: LEFT, ROOT, RIGHT
    def buildPreIn(self, preorder=None, inorder=None):
        self.index = 0 # We start with the 0th index
        hashMap = {n:i for i, n in enumerate(inorder)} #We then move to a hashMap
        # Our hashMap where we store data which is created from inorder --> LEFT, ROOT, RIGHT
        # {
            # 9: 0, 
            # 3: 1, 
            # 15: 2, 
            # 20: 3, 
            # 7: 4
        # }
        def helper(lo, hi):
            if lo > hi:
                return None
            node = TreeNode()
            #preorder: [3, 9, 20, 15, 7]
            node.val = preorder[self.index]
            self.index += 1
            node.left = helper(lo, hashMap[node.val]-1)
            node.right = helper(hashMap[node.val]+1, hi)
            return node
        return helper(0, len(preorder)-1)
    
    


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
print("Visualize: ", Solution().visualizePreOrder(rootData, 2))
# print("InOrder: ", Solution().inOrder(rootData))
# print("PostOrder: ", Solution().postOrder(rootData))

# rootTree = Solution().buildTree(inorder, postOrder)
# print("Construct Binary Tree: ", Solution().preOrder(rootTree))

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# newRoot = Solution().buildPreIn(preorder, inorder)