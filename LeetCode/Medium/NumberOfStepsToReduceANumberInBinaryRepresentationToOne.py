"""
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

    If the current number is even, you have to divide it by 2.

    If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.


Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:

Input: s = "1"
Output: 0


Constraints:
    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'

"""


class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        decimal_val = int(s, 2)
        steps = 0
        
        while decimal_val != 1:
            if decimal_val % 2 != 0:
                decimal_val += 1
            else:
                decimal_val /= 2
            steps += 1
            
        return steps
    
    def numStepss(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Iterate from right to left, skipping the first bit
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry
            
            if digit == 1:
                # It's odd: requires 2 steps (add 1 to make it even, then divide by 2)
                steps += 2
                carry = 1
            else:
                # It's even: requires 1 step (divide by 2)
                steps += 1
            
        return steps + carry
    
import time

solution = Solution()

start_time = time.time()
print(solution.numSteps("1101"))
end_time = time.time()
print(f"Time taken: {end_time - start_time:.6f} seconds")

start_time = time.time()
print(solution.numSteps("10"))
end_time = time.time()
print(f"Time taken: {end_time - start_time:.6f} seconds")

start_time = time.time()
print(solution.numSteps("1"))
end_time = time.time()
print(f"Time taken: {end_time - start_time:.6f} seconds")

start_time = time.time()
print(solution.numSteps("1111"))
print(f"Time taken: {time.time() - start_time:.6f} seconds")

start_time = time.time()
print(solution.numSteps("11111"))
print(f"Time taken: {time.time() - start_time:.6f} seconds")

start_time = time.time()
print(solution.numStepss("1101"))
print(f"Time taken: {time.time() - start_time:.6f} seconds")
