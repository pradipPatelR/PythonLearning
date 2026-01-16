"""
Given an integer x, return true if x is a, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -231 <= x <= 231 - 1

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        
        updateNumber = x
        reversed_num = 0
        
        while updateNumber > 0:
            reversed_num = (reversed_num * 10) + (updateNumber % 10)
            updateNumber //= 10
        return x == reversed_num 
        
        
        
solution = Solution()
print(solution.isPalindrome(x=123))
print(solution.isPalindrome(x=1))
print(solution.isPalindrome(x=121))
print(solution.isPalindrome(x=-121))
print(solution.isPalindrome(x=10))
print(solution.isPalindrome(x=0))

