"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
    
        map_s_t = {}
        map_t_s = {}
    
        for char_s, char_t in zip(s, t):
            if char_s in map_s_t:
                if map_s_t[char_s] != char_t:
                    return False
            else:
                map_s_t[char_s] = char_t
            
            if char_t in map_t_s:
                if map_t_s[char_t] != char_s:
                    return False
            else:
                map_t_s[char_t] = char_s
                
        return True

        # # 2. Other Way
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    
solution = Solution()
print(solution.isIsomorphic("egg", "add"))  # Output: True
print(solution.isIsomorphic("f11", "b23"))  # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True
print(solution.isIsomorphic("abc", "def"))  # Output: True
print(solution.isIsomorphic("ab", "aa"))  # Output: False
