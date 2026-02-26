"""
Reverse bits of a given 32 bits signed integer.


Example 1:

Input: n = 43261596

Output: 964176192

Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110


Constraints:
    0 <= n <= 231 - 2
    n is even.

"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        # We must iterate exactly 32 times for a 32-bit integer
        for i in range(32):
            # 1. Shift result to the left to make room for the next bit
            result <<= 1

            # 2. Get the last bit of n using bitwise AND
            last_bit = n & 1

            # 3. Add that bit to our result using bitwise OR
            result |= last_bit

            # 4. Shift n to the right to process the next bit
            n >>= 1

        return result
    
    # ----------------------------------
    
        # binary_str = format(n, '032b')
        # reversed_str = binary_str[::-1]
        # return int(reversed_str, 2)
    
    # ----------------------------------
        
        # binary_str = format(n, 'b')
        
        # count = len(binary_str)
        
        # if count != 32:
        #     prefixString = "0" * (32 - count)
        #     binary_str = prefixString + binary_str
           
        # reversed_binary_str = binary_str[::-1]
        
        # return int(reversed_binary_str, 2)
        
        
solution = Solution()
print(solution.reverseBits(7))
print(solution.reverseBits(43261596))
print(solution.reverseBits(2147483644))