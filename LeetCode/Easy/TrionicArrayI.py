"""
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.


Example 1:

Input: nums = [1,3,5,4,2,6]
Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
Example 2:

Input: nums = [2,1,3]
Output: false

Explanation:

There is no way to pick p and q to form the required three segments.


Constraints:

3 <= n <= 100
-1000 <= nums[i] <= 1000

"""

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        
        p = 0
        while p < n - 1 and nums[p] < nums[p + 1]:
            p += 1
        
        if p == 0 or p == n - 1:
            return False
        
        q = p
        while q < n - 1 and nums[q] > nums[q + 1]:
            q += 1
        
        if q == p or q == n - 1:
            return False
        
        for i in range(q, n - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True
    
# Example usage:
solution = Solution()
print(solution.isTrionic([1, 3, 5, 4, 2, 6]))  # Output: true
print(solution.isTrionic([2, 1, 3]))  # Output: false   
print(solution.isTrionic([1, 2, 3]))  # Output: false
print(solution.isTrionic([3, 2, 1]))  # Output: false
print(solution.isTrionic([1, 3, 2, 4]))  # Output: false
print(solution.isTrionic([1, 2, 1, 2]))  # Output: false
print(solution.isTrionic([1, 2, 3, 2, 1, 2, 3]))  # Output: true
