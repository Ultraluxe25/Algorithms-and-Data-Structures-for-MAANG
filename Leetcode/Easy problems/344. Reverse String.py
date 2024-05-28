"""
344. Reverse String
Solved 26.05.2024
Easy

Hint
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

# Solution (Two pointers)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0  # Two pointers
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s
