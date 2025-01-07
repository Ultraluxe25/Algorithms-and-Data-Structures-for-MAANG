"""
1408. String Matching in an Array
Solved 07.01.2024
Easy
Topics: Array, String, String Matching

Given an array of string words, return all strings in words that is a substring of another word. 
You can return the answer in any order.

A substring is a contiguous sequence of characters within a string


Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.


Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".


Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
"""

# Solution (Beated 100% runtime, O(n^2))
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        message = ' '.join(words)
        result = []

        for word in words:
            if message.count(word) > 1:
                result.append(word)

        return result
