"""
1790. Check if One String Swap Can Make Strings Equal
Solved 05.02.2025
Easy
Topics: Hash Table, String, Counting

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string 
(not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. 
Otherwise, return false.


Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".


Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.


Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

# Solution (Beats 100% time complexity)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        match = 0
        unmatch = []
        n = len(s1)

        for i in range(n):
            if s1[i] == s2[i]:
                match += 1
            else:
                if len(unmatch) > 2:
                    return False
                    
                unmatch.append(s1[i] + s2[i])

        if match == n or ((match == n - 2) and unmatch[0] == unmatch[1][::-1]):
            return True
        else:
            return False
