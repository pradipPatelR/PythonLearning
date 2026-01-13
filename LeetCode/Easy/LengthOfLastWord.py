"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 'Substring' consisting of non-space characters only.
 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.

"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # wordCounter = 0
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] != ' ':
        #         wordCounter += 1
        #     else:
        #         if wordCounter > 0:
        #             break
            
        # return wordCounter
    
        # Strip trailing spaces and split the string into words
        words = s.strip().split(' ')
        # Return the length of the last word
        return len(words[-1])
    
# Example usage:
sol = Solution()
s = "Hello World"
length = sol.lengthOfLastWord(s)
print(length)  # Output: 5

s = "   fly me   to   the moon  "
length = sol.lengthOfLastWord(s)
print(length)  # Output: 4

s = "luffy is still joyboy"
length = sol.lengthOfLastWord(s)
print(length)  # Output: 6

s = "a "
length = sol.lengthOfLastWord(s)
print(length)  # Output: 1

s = " "
length = sol.lengthOfLastWord(s)
print(length)  # Output: 1
