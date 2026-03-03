"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = nums[0]
        freq = 1
        
        for i in range(1, n):
            if res == nums[i]:
                freq = freq + 1
            else:
                freq = 1
                res = nums[i]
                
            if freq > (n/2):
                return res
        
        return res
    
solution = Solution()
print(solution.majorityElement([3,2,3]))
print(solution.majorityElement([2,2,1,1,1,2,2]))

