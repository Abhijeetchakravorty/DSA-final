class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class ChildNode:
    def __init__(self, val=None, next=None, prev=None, child=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.child = child

class MyLinkedList:      
    def __init__(self):
        self.head = None
    
    def createDynamicSinglyList(self, arr):
        self.head = Node(arr[0])
        temp = self.head
        i = 1
        while(i<len(arr)):
            temp.next = Node(arr[i])
            i += 1
            temp = temp.next
            
        return self.head
    
    def createDynamicDoublyList(self, arr):
        self.head = Node(arr[0]) #set first head for returning the head 
        # 1 --> 2 --> 3
        temp = self.head #set head to a temp variable for the iteration
        i = 1 # set a counter for iterating over an array
        while(i<len(arr)):
            temp.next = Node(arr[i])
            i += 1
            temp.next.prev = temp
            temp = temp.next
        
        return self.head
                
    def printList(self, head):
        temp = head
        while(temp):
            print(temp.val)
            temp = temp.next
    
    def printDoublyList(self, head):
        temp = head
        while(temp):
            if (temp.prev):
                print(temp.val, temp.prev.val)
            else:
                print(temp.val, None)
            temp = temp.next

    def reverseList(self, head):
        prev = None
        while(head):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        # A--B--C--C--B--A
        while(fast and fast.next):
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if (fast):
            slow = slow.next #For odd number of items
        
        while(rev and rev.val == slow.val):
            rev, slow = rev.next, slow.next
        
        return not rev
    
    def mergeTwoSortedList(self, l1, l2):
        ## 1-3-5-7-9
        ## 2-4-6-8-10
        out = output = Node(0)
        while((l1 != None) and (l2 != None)):
            if (l1.val < l2.val):
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next
        output.next = (l1 or l2)
        return out.next
    
    def addTwoNumbers(self, l1, l2):
        result_tail = Node(0)
        result = result_tail
        carry = 0
        
        while(l1 or l2 or carry):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)
            
            result.next = Node(out)
            result = result.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return result_tail.next
    
    def flattenList(self, head):
        self.printList(head)
    
    
    
    
        

arr = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
head = MyLinkedList()
# list = head.createDynamicSinglyList(arr)
# print(head.isPalindrome(list))
# newList = head.reverseList(list)  # reverse List
# print("//////////////////////")
# print(head.isPalindrome(list))


# list2 = head.createDynamicSinglyList(arr2)
# head.printList(list)
# head.printList(list2)
# head.printList(list2)
# mergedList = head.mergeTwoSortedList(list, list2)
# head.printList(mergedList)
# print("//////////////////////")
# print("//////////////////////")
# sumList = head.addTwoNumbers(list, list2)
# head.printList(sumList)


# doublyList = head.createDynamicDoublyList(arr)
# head.printDoublyList(doublyList)


head.val = ChildNode(1)
head.next = ChildNode(2)
head.next.next = ChildNode(3)
head.next.next.next = ChildNode(4)
head.next.next.next.next = ChildNode(5)
head.next.next.next.next.next = ChildNode(6)
head.next.next.child = ChildNode(7)
head.next.next.child.next = ChildNode(8)