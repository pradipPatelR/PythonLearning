r"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.


Example 1:

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
       1
     /   \
    0     1
   / \   / \
  0   1 0   1

Example 2:

Input: root = [0]
Output: 0


Constraints:
    The number of nodes in the tree is in the range [1, 1000].
    Node.val is 0 or 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val:int=0, left:int=None, right:int=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        total_sum = 0
        stack = [(root, 0)]

        while stack:
            node, current_val = stack.pop()
            if node:
                current_val = (current_val << 1) | node.val
                if not node.left and not node.right:
                    total_sum += current_val
                else:
                    stack.append((node.right, current_val))
                    stack.append((node.left, current_val))

        return total_sum
        
        # def dfs(node, current_val):
        #     if not node:
        #         return 0

        #     # Shift current value left and add current bit
        #     # This is equivalent to: current_val * 2 + node.val
        #     current_val = (current_val << 1) | node.val

        #     # If it's a leaf node, return the completed binary value
        #     if not node.left and not node.right:
        #         return current_val

        #     # Recursively sum values from left and right subtrees
        #     return dfs(node.left, current_val) + dfs(node.right, current_val)

        # return dfs(root, 0)
    
solution = Solution()

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

print(solution.sumRootToLeaf(root))

root = TreeNode(0)

print(solution.sumRootToLeaf(root))

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)

print(solution.sumRootToLeaf(root))

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)

print(solution.sumRootToLeaf(root))



