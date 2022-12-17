class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:      
    def __init__(self):
        self.head = None
    
    def createDynamicList(self, arr):
        self.head = Node(arr[0])
        temp = self.head
        i = 1
        while(i<len(arr)):
            temp.next = Node(arr[i])
            i += 1
            temp = temp.next
            
        return self.head
                
    def printList(self, head):
        temp = head
        while(temp):
            print(temp.val)
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
        

arr = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
head = MyLinkedList()
list = head.createDynamicList(arr)
# print(head.isPalindrome(list))
# newList = head.reverseList(list)  # reverse List
print("//////////////////////")
# print(head.isPalindrome(list))


list2 = head.createDynamicList(arr2)
# head.printList(list)
# head.printList(list2)
# head.printList(list2)
mergedList = head.mergeTwoSortedList(list, list2)
head.printList(mergedList)
