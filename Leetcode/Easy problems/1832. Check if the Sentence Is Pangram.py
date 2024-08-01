"""
1832. Check if the Sentence Is Pangram
Solved 01.08.2024
Easy
Topics: Hash Table, String

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.


Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

# Solution 1 (Hash Table using Counter)
from string import ascii_lowercase
from collections import Counter

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        frequency = Counter(sentence)
        
        for i in ascii_lowercase:
            if frequency.get(i) is None:
                return False

        return True


# Solution 1 (Hash set)
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
    