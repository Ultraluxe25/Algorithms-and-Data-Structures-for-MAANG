"""
1002. Find Common Characters
Solved 05.06.2024
Easy

Given a string array words, return an array of all characters that show up in all strings within the words 
(including duplicates). You may return the answer in any order.

 
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]


Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""

# Solution 1 (With sorting)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Looking for longest substring
        words.sort(reverse=True, key=len)  # Time O(nlogn)
        reference = set(words[0])  # Unique values of the longest word
        print(reference)
        
        result = []
        for char in reference:
            repeat = min([word.count(char) for word in words])
            result.extend([char] * repeat)

        return result        
        

# Solution 2 (Without sorting)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        reference = set(words[0])
        result = []
        
        for char in reference:
            repeat = min([word.count(char) for word in words])
            result.extend([char] * repeat)

        return result        
        