"""
2816. Double a Number Represented as a Linked List
Solved 07.05.2024
Medium

Hint
You are given the head of a non-empty linked list representing a non-negative integer without 
leading zeroes.

Return the head of the linked list after doubling it.


Example 1:


Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. 
Hence, the returned linked list represents the number 189 * 2 = 378.


Example 2:


Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. 
Hence, the returned linked list reprersents the number 999 * 2 = 1998. 
 

Constraints:

The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, 
except the number 0 itself.

Hint 1
Traverse the linked list from the least significant digit to the most significant digit and multiply each node's value by 2

Hint 2
Handle any carry-over digits that may arise during the doubling process.

Hint 3
If there is a carry-over digit on the most significant digit, create a new node with that value and point it to the start of the given linked list and return it.
"""

# Solution 1 (Brute force)
import sys
sys.set_int_max_str_digits(0)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Traverse through initial linked list with gather each element
        number = ''
        current = head  # ListNode dtype
        while current is not None:
            number += str(current.val)
            current = current.next

        # Values for new linked list
        new_number = (str(int(number) * 2))
        new_values = [int(i) for i in new_number]

        # Create new linked list
        result_list = ListNode(new_values[0])
        current = result_list
        for i in new_values[1:]:
            current.next = ListNode(i)
            current = current.next

        return result_list            
