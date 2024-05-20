"""
383. Ransom Note
Solved 20.05.2024
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine 
and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false


Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false


Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# Solution 1 (without Counter)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}

        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else:
                magazine_dict[i] += 1

        for i in ransomNote:
            if i not in magazine_dict or magazine_dict[i] < 1:
                return False
            magazine_dict[i] -= 1
        
        return True

# Solution 2 (with Counter)
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = Counter(magazine)

        for i in ransomNote:
            if i not in magazine_dict or magazine_dict[i] < 1:
                return False
            magazine_dict[i] -= 1
        
        return True
