"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst_l1 = []
        lst_l2 = []

        while l1.next is not None: 
            lst_l1.append(str(l1.val))
            l1 = l1.next
        lst_l1.append(str(l1.val))

        while l2.next is not None: 
            lst_l2.append(str(l2.val))
            l2 = l2.next
        lst_l2.append(str(l2.val))

        print(lst_l1)
        numbers_1 = int(''.join(lst_l1[::-1]))
        numbers_2 = int(''.join(lst_l2[::-1]))

        result = numbers_1 + numbers_2
        lst = [int(x) for x in str(result)][::-1]

        response = ListNode()
        first_element = response

        n = len(lst)
        for index, value in enumerate(lst):
            response.val = value
            if index == n - 1:
                break

            response.next = ListNode()
            response = response.next
            
        response.next = None    
        return first_element
        