"""
20. Valid Parentheses
Solved 30.09.2024
Easy
Topics: String, Stack

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true



Example 2:

Input: s = "()[]{}"

Output: true



Example 3:

Input: s = "(]"

Output: false



Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Best Solution
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in parentheses:
                stack.append(char)
            else:  # Check whether stack is not empty
                if not stack or parentheses[stack.pop()] != char:
                    return False
        
        return not stack  # Check whether stack is already empty
