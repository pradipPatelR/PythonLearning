"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).


Example 1:

Input: n = 11
Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128
Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645
Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.


Constraints:
1 <= n <= 2^31 - 1
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return format(n, 'b').count("1")


solution = Solution()
print(solution.hammingWeight(11))  # Output: 3
print(solution.hammingWeight(128))  # Output: 1
print(solution.hammingWeight(2147483645))  # Output: 30
print(solution.hammingWeight(1))  # Output: 1
print(solution.hammingWeight(0))  # Output: 0
print(solution.hammingWeight(4294967295))  # Output: 32
