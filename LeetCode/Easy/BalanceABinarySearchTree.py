"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]


Constraints:
    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def inorder_traversal(aRoot):
            # In-order traversal to get a sorted array of node values
            if not aRoot:
                return []
            return inorder_traversal(aRoot.left) + [aRoot.val] + inorder_traversal(aRoot.right)
        
        def sorted_array_to_bst(sorted_vals):
            # Build a balanced BST from the sorted values
            if not sorted_vals:
                return None
            mid = len(sorted_vals) // 2
            nroot = TreeNode(sorted_vals[mid])  # Create a root node with the middle value
            nroot.left = sorted_array_to_bst(sorted_vals[:mid])  # Left subtree
            nroot.right = sorted_array_to_bst(sorted_vals[mid+1:])  # Right subtree
            return nroot
        
        if not root:
            return None
        
        sorted_vals = inorder_traversal(root)
        return sorted_array_to_bst(sorted_vals)


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        # Print the current node with indentation based on its level
        print(" " * (level * 4) + prefix + str(root.val))
        # Recursively print left and right subtrees
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")
    
# end def

solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)

print_tree(root)

aroot = solution.balanceBST(root)

print_tree(aroot)