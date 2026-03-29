"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


Constraints:

The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= val <= 50
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return dummy.next
    

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=' ')
        current = current.next
    print()

solution = Solution()
# Example 1
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
val = 6 
new_head = solution.removeElements(head, val)
# Print the new linked list
print_linked_list(new_head)

# Example 2
head = None
val = 1
new_head = solution.removeElements(head, val)
# Print the new linked list
print_linked_list(new_head)

# Example 3
head = ListNode(1, ListNode(7, ListNode(7, ListNode(7, ListNode(3)))))
val = 7
new_head = solution.removeElements(head, val)
# Print the new linked list
print_linked_list(new_head)
