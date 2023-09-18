# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr_list1 = list1
        curr_list2 = list2

        if curr_list1.val <= curr_list2.val:
            head = curr_list1
        else:
            head = curr_list2

        # compare curr_list1 and curr_list2, whichever is less comes next, to properly
        # splice, save the next node of the curr_list and insert the node, then
        prev_list1 = curr_list1
        prev_list2 = curr_list2
        curr_list1 = curr_list1.next
        curr_list2 = curr_list2.next
        while curr_list1 or curr_list2:
            # insert curr_list1 node behind curr_list2 node
            if curr_list1.val <= curr_list2.val:
                prev_list1 = curr_list1
                curr_list1 = curr_list1.next
                
            else:
                prev_list2 = curr_list2
                curr_list2.next = curr_list1
