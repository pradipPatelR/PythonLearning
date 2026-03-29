"""
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []


Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current      
            current = next_node

        return prev

# Example usage:

solution = Solution()

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=' ')
        current = current.next
    print()

# Creating a linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: 5 4 3 2 1

head = ListNode(1, ListNode(2))
reversed_head = solution.reverseList(head)
print_linked_list(reversed_head)  # Output: 2 1

head = None
reversed_head = solution.reverseList(head)  
print_linked_list(reversed_head)  # Output: (prints nothing)

