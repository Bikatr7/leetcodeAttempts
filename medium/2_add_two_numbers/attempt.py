## Bikatr7
## 2024-07-16
## 2. Add Two Numbers (Medium)

## Description:

## You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
## You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Constraints:

## The number of nodes in each linked list is in the range [1, 100].
## 0 <= Node.val <= 9
## It is guaranteed that the list represents a number that does not have leading zeros.

## Given my code style's verbosity it is recommended to submit without any comments, spacing, type hints, or ()

## built-in libraries
import typing

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:typing.Optional[ListNode], l2:typing.Optional[ListNode]) -> typing.Optional[ListNode]:

        head = current = ListNode()
        carry = 0

        while(l1 or l2 or carry):

            ## if l1 is not None, val1 = l1.val, else val1 = 0
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            ## divmod returns a tuple of two values, the first is the division, the second is the remainder
            carry, sum = divmod(val1 + val2 + carry, 10)
            
            current.next = ListNode(sum)
            current = current.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return head.next
    
## Submission Code:
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = current = ListNode()
        carry = 0
        while(l1 or l2 or carry):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, sum = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(sum)
            current = current.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return head.next