"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
    
    
# Example usage:
solution = Solution()
# Creating first linked list: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Creating second linked list: 1 -> 3 -> 4
list2 = ListNode(5, ListNode(3, ListNode(4)))
merged_list = solution.mergeTwoLists(list1, list2)
# Print merged linked list
while merged_list:
    print(merged_list.val, end=" -> " if merged_list.next else "\n")
    merged_list = merged_list.next


list1 = None
list2 = ListNode(0)
merged_list = solution.mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, end=" -> " if merged_list.next else "\n")
    merged_list = merged_list.next
    
list1 = ListNode(2)
list2 = ListNode(1)
merged_list = solution.mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, end=" -> " if merged_list.next else "\n")
    merged_list = merged_list.next

list1 = ListNode(5)
list2 = ListNode(1, ListNode(2, ListNode(4)))
merged_list = solution.mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, end=" -> " if merged_list.next else "\n")
    merged_list = merged_list.next

