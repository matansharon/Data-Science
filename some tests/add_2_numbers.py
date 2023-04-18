#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example 1:
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

#Example 2:
#Input: l1 = [0], l2 = [0]
#Output: [0]

#write the code here

#Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        curr = head
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return head.next
    


#Test
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(l1.val)
print(l1.next.val)
print(l1.next.next.val)


#another test
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

#another test
l3 = ListNode(0)
l4 = ListNode(0)

