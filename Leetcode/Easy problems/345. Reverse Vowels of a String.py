"""
345. Reverse Vowels of a String
Solved 21.05.2024
Easy

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "hello"
Output: "holle"


Example 2:

Input: s = "leetcode"
Output: "leotcede"
 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

# Solution 1 (brute force)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        temp = []

        for i in s:
            if i.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels.append(i)
                temp.append('_')
            else:
                temp.append(i)

        vowels.reverse()
        i = 0  # Vowel's pointer
        j = 0  # Temp's pointer
        while i < len(vowels):
            if temp[j] == '_':
                temp[j] = vowels[i]
                i += 1
            j += 1

        return ''.join(temp)
        

# Solution 2 (using stack)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []  # Stack
        temp = []

        for i in s:
            if i.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels.append(i)
                temp.append('_')
            else:
                temp.append(i)

        i = 0
        while vowels:
            if temp[i] == '_':
                temp[i] = vowels.pop()
            i += 1
        
        return ''.join(temp)
        