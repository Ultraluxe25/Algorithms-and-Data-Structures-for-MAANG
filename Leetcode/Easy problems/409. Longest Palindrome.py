"""
409. Longest Palindrome
Solved 04.06.2024
Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.


Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_table = {}
        result = 0
        central_char = False  # Whether odd elements in the hash-table

        # Build hash_table
        for i in range(len(s)):
            if s[i] in hash_table:
                hash_table[s[i]] += 1
            else:
                hash_table[s[i]] = 1

        # Traversing the hash-table
        print(sorted(hash_table.values()))
        for _, value in hash_table.items():
            if value % 2 == 0:
                result += value
            else:
                result += value - 1
                central_char = True

        return result + central_char

        # You are avoiding all the odd length occurence and consider only the longest but the question say diffrent 
        # we can rearange and and can make palindrome from all the string like if occurence id 7 then we can make by 6 letter 
        # ans can be handle 1 separate.
