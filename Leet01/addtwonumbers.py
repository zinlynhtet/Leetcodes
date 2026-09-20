#demo'https://share.gemini.google/tJ1bkDrfNUrD'
# https://leetcode.com/problems/add-two-numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def list_to_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = Solution().addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))
    
    # Step-by-step explanation:
        # 1. Create a dummy node to help build the result list without special-case handling.
        # 2. Keep a pointer called current to the last node in the result list.
        # 3. Traverse both linked lists while either list still has a node or a carry remains.
        # 4. For each position, add the current digits and any previous carry.
        # 5. Compute the new digit as total % 10 and store it in a new node.
        # 6. Compute the next carry as total // 10.
        # 7. Move each input pointer forward if it exists.
        # 8. Return dummy.next, which is the head of the final sum list.
        #
        # Time complexity: O(max(n, m))
        # Space complexity: O(max(n, m)) for the output list, excluding input storage.