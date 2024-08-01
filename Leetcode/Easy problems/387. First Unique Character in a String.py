"""
387. First Unique Character in a String
Solved 01.08.2024
Easy
Topics: Hash Table, String, Queue, Counting

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 
Example 1:

Input: s = "leetcode"
Output: 0


Example 2:

Input: s = "loveleetcode"
Output: 2


Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

# Solution 1 (Hash table with dict)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}

        for i in s:
            if i in unique:
                unique[i] += 1
            else:
                unique[i] = 1

        for idx, value in enumerate(s):
            if unique.get(value) == 1:
                return idx

        return -1


# Solution 2 (Hash table with Counter)
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = Counter(s)

        for idx, value in enumerate(s):
            if unique.get(value) == 1:
                return idx

        return -1
