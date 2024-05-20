"""
1768. Merge Strings Alternately
Solved 05.05.2024
Easy

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.

Return the merged string.

 
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

# Solution 1
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        n = l1  # l1 == l2
        end = ''
        result = ''

        if l1 > l2:
            end = word1[l2:]
            n = l2
        elif l1 < l2:
            end = word2[l1:]
            n = l1

        for i in range(n):
            result += word1[i] + word2[i]
        
        return result + end
    

# Solution 2
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        result = ''

        i = 0  # Two pointers
        j = 0

        while i < l1 and j < l2:
            result += word1[i] + word2[j]
            i += 1
            j += 1
        
        return result + word1[i:] + word2[j:]       


# Solution 3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        result = []

        i = 0  # Two pointers
        j = 0

        while i < l1 and j < l2:
            result.append(word1[i] + word2[j])
            i += 1
            j += 1

        result.append(word1[i:] + word2[j:])
        
        return ''.join(result)       
