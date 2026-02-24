"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701


Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].

"""

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0

        for char in columnTitle:
            # Treat this as a base-26 number system
            # A=1, B=2, ..., Z=26
            result = result * 26 + (ord(char) - ord('A') + 1)
        
        return result
    
    
    
# Test cases
solution = Solution()

# Test with example cases
print(solution.titleToNumber("A"))      # Expected: 1
print(solution.titleToNumber("B"))      # Expected: 2
print(solution.titleToNumber("Z"))      # Expected: 26
print(solution.titleToNumber("AA"))     # Expected: 27
print(solution.titleToNumber("AB"))     # Expected: 28
print(solution.titleToNumber("ZY"))     # Expected: 701
print(solution.titleToNumber("FXSHRXW")) # Expected: 2147483647