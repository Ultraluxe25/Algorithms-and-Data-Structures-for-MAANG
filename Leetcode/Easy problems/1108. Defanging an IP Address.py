"""
1108. Defanging an IP Address
Solved 02.07.2024

Easy

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"


Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
"""

# Solution 1 (Brute force)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip = ''
        for i in address:
            ip = ip + '[.]' if i == '.' else ip + i

        return ip


# Solution 2 (Too short)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
