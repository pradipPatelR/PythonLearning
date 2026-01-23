"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a Height-Balanced binary search tree.


Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
    
solution = Solution()

def print_tree(node:TreeNode = None, level=0, prefix="Root:"):
    if node is not None:
        print(" " * (level * 4) + prefix + " " + str(node.val))
        print_tree(node.left, level + 1, prefix="L---")
        print_tree(node.right, level + 1, prefix="R---")
    else:
        print(" " * (level * 4) + prefix + " None")

print_tree(solution.sortedArrayToBST([-10,-3,0,5,9]))
print(' ')
print_tree(solution.sortedArrayToBST([1,3]))
print(' ')
print_tree(solution.sortedArrayToBST([-4,-3,-2,-1,0,1,2,3,4]))
print(' ')
print_tree(solution.sortedArrayToBST([0]))
print(' ')
print_tree(solution.sortedArrayToBST([1,2,3,4,5,6,7,8,9,10]))
print(' ')
print_tree(solution.sortedArrayToBST([-1000,-500,0,500,1000]))