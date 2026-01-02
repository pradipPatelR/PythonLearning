"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.


"""


from sys import prefix


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        print("strings:", strs)
        # sort the list
        strs.sort()
        print("sorted strings:", strs)

        first = strs[0]
        last = strs[-1]
        prefix = ""

        print("first string:", first)
        print("last string:", last)

        # compare characters of first and last string
        for i in range(len(first)):
            print("comparing characters:", first[i], last[i])
            if i >= len(last) or first[i] != last[i]:
                break
            prefix += first[i]
            print("current prefix:", prefix)
        return prefix
    

solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))     # Output: "" 
