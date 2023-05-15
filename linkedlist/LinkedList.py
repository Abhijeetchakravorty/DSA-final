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


class RandomNode:
    def __init__(self, val=None, next=None, prev=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class MyLinkedList:
    def __init__(self):
        self.head = None

    def createDynamicSinglyList(self, arr):
        self.head = Node(arr[0])
        temp = self.head
        i = 1
        while (i < len(arr)):
            temp.next = Node(arr[i])
            i += 1
            temp = temp.next

        return self.head

    def createDynamicDoublyList(self, arr):
        self.head = Node(arr[0])  # set first head for returning the head
        # 1 --> 2 --> 3
        temp = self.head  # set head to a temp variable for the iteration
        i = 1  # set a counter for iterating over an array
        while (i < len(arr)):
            temp.next = Node(arr[i])
            i += 1
            temp.next.prev = temp
            temp = temp.next

        return self.head

    def printList(self, head):
        temp = head
        while (temp):
            print(temp.val)
            temp = temp.next

    def printDoublyList(self, head):
        temp = head
        while (temp):
            if (temp.prev):
                print(temp.val, temp.prev.val)
            else:
                print(temp.val, None)
            temp = temp.next

    def reverseList(self, head):
        prev = None
        while (head):
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        # A--B--C--C--B--A
        while (fast and fast.next):
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if (fast):
            slow = slow.next  # For odd number of items

        while (rev and rev.val == slow.val):
            rev, slow = rev.next, slow.next

        return not rev

    def mergeTwoSortedList(self, l1, l2):
        # 1-3-5-7-9
        # 2-4-6-8-10
        out = output = Node(0)
        while ((l1 != None) and (l2 != None)):
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

        while (l1 or l2 or carry):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)

            result.next = Node(out)
            result = result.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result_tail.next

    def flattenList(self, head):
        temp = head
        st = []
        while (temp):  # rotating over the temp list
            if (temp.child):  # check if temp has child
                if (temp.next):  # check if temp has next
                    # append the next element if it exists
                    st.append(temp.next)
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None
            elif not temp.next and len(st):
                node = st.pop()
                temp.next = node
                node.prev = temp
            temp = temp.next
        return head

    # What can I do to copy random pointer
    #

    def randomPointer(self, head):
        old_address_to_index = {}  # created a dictionary
        new_address = []  # created a new array

        current = head  # pointed current to head
        i = 0  # pointed i to 0

        # We are iterating over current head and creating new nodes and adding adding data to old_address_to_index dictionary
        # When use the key as old address and use i
        # and finally adding to array called new_address
        while current is not None:  # while loop
            new_node = RandomNode(current.val)
            old_address_to_index[current] = i
            new_address.append(new_node)

            current = current.next
            i += 1

        # And at the end we add a null pointer
        new_address.append(None)

        # setting head to a variable
        original = head
        # settig i to 0
        i = 0

        # while original is not none
        while original is not None:
            new_node = new_address[i]  # NOw new address with index is at i
            new_node.next = new_address[i+1]  # The next address is set
            if original.random is not None:  # Now we start setting the random parameter for the new node
                # the new random parameter goes with new_address
                new_node.random = new_address[old_address_to_index[original.random]]

            original = original.next
            i += 1

        return new_address[0]

    def rotateList(self, head, k):
        node = head
        count = 0
        while node != None:
            count += 1
            node = node.next
        if count == 0:
            return None
        
        realCount = k % count
        
        if realCount == 0:
            return head
        
        node = head
        for i in range(count - realCount - 1):
            node = node.next
        newHead = node.next
        node.next = None
        
        node = newHead
        while node.next != None:
            node = node.next
        node.next = head

        return newHead
    

        
        
        
        
        
        
        

arr = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
headOne = MyLinkedList()

#Rotate List
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

newList = headOne.rotateList(head, 2)
headOne.printList(newList)





























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


# For flattening linked list start
# head = ChildNode(1)
# head.next = ChildNode(2)
# head.next.next = ChildNode(3)
# head.next.next.next = ChildNode(4)
# head.next.next.next.next = ChildNode(5)
# head.next.next.next.next.next = ChildNode(6)
# head.next.next.child = ChildNode(7)
# head.next.next.child.next = ChildNode(8)
# head.next.next.child.next.child = ChildNode(11)
# head.next.next.child.next.child.next = ChildNode(12)
# head.next.next.child.next.next = ChildNode(9)
# head.next.next.child.next.next.next = ChildNode(10)

# multiLevelList = head
# flatten = headOne.flattenList(multiLevelList)
# headOne.printList(flatten)
# for flattening linked list end


# For copying list with random pointer start
# head1 = RandomNode(7)
# head2 = RandomNode(13)
# head3 = RandomNode(11)
# head4 = RandomNode(10)
# head5 = RandomNode(1)

# head1.next = head2
# head2.next = head3
# head3.next = head4
# head4.next = head5

# head1.random = None
# head2.random = head1
# head3.random = head5
# head4.random = head3
# head5.random = head1

# newLL = headOne.addRandomPointer(head1)
# headOne.printList(newLL)
# For copying list with random pointer end
