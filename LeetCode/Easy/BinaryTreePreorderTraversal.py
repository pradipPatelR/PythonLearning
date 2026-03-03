"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Explanation:


Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []
Output: []

Example 4:

Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        def preorder(node):
            if node:
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return result
    
# Example usage:
solution = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(solution.preorderTraversal(root))  # Output: [1, 2, 3]

root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)

print(solution.preorderTraversal(root))  # Output: [1, 2, 4, 5, 6, 7, 3, 8, 9]