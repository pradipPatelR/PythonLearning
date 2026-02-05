"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = 0
        R = len(s) - 1
        
        while (L < R):
            if not s[L].isalnum():
                L += 1
                continue
            
            if not s[R].isalnum():
                R -= 1
                continue
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True
    
        # filtered_s = "".join(char for char in s if char.isalnum()).lower()
        # # Compare string with its reverse
        # return filtered_s == filtered_s[::-1]
    
solution = Solution()
str = "A man, a plan, a canal: Panama"
print(f"{str}\n is Palindrome =", solution.isPalindrome(str))
str = "race a car"
print(f"{str}\n is Palindrome =", solution.isPalindrome(str))
str = " "
print(f"{str}\n is Palindrome =", solution.isPalindrome(str))
str = "race a ecar"
print(f"{str}\n is Palindrome =", solution.isPalindrome(str))
