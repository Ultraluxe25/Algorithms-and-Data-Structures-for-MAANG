"""
2487. Remove Nodes From Linked List
Solved 06.05.2024
Medium

Hint
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 
Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.


Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""

# Solution 1 (Brute force)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Gather values in list
        lst = []
        current = head
        while current is not None:
            lst.append(current.val)
            current = current.next

        # Save reversed values in ascending order
        lst.reverse()
        new_lst = [lst[0]]
        pointer = lst[0]
        for i in range(len(lst) - 1):
            if lst[i + 1] >= pointer:
                new_lst.append(lst[i + 1])
                pointer = lst[i + 1]
        
        # Create new linked list
        new_lst.reverse()
        result = ListNode(val=new_lst[0])
        current = result
        for val in new_lst[1:]:
            current.next = ListNode(val)
            current = current.next

        return result
    