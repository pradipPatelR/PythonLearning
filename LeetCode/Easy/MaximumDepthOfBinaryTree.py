"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100

"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
solution = Solution()
print(solution.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # Example usage
print(solution.maxDepth(TreeNode(1, None, TreeNode(2))))  # Example usage
print(solution.maxDepth(None))  # Example usage
print(solution.maxDepth(TreeNode(1)))  # Example usage
print(solution.maxDepth(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))))  # Example usage
print(solution.maxDepth(TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))))  # Example usage