"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
    1 <= n <= 45

"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """ 
        prev1 = 1
        prev2 = 1
  
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
            
        return prev1
        """
        
        if n <= 2:
            return n
        
        first = 1
        second = 2
        
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return second

# Example usage:
sol = Solution()
n = 2
ways = sol.climbStairs(n)
print(ways)  # Output: 2

n = 3
ways = sol.climbStairs(n)
print(ways)  # Output: 3

n = 4
ways = sol.climbStairs(n)
print(ways)  # Output: 5

n = 5
ways = sol.climbStairs(n)
print(ways)  # Output: 8

n = 6
ways = sol.climbStairs(n)
print(ways)  # Output: 13

n = 7
ways = sol.climbStairs(n)
print(ways)  # Output: 21

n = 8
ways = sol.climbStairs(n)
print(ways)  # Output: 34

n = 9
ways = sol.climbStairs(n)
print(ways)  # Output: 55

n = 10
ways = sol.climbStairs(n)
print(ways)  # Output: 89

n = 45
ways = sol.climbStairs(n)
print(ways)  # Output: 1836311903