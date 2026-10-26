"""LeetCode 21: Merge Two Sorted Lists.

Merge two ascending linked lists by relinking their existing nodes.
Time: O(n + m). Extra space: O(1) (excluding the returned list's nodes).
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # At most one list still contains nodes; append it without copying.
        tail.next = list1 if list1 is not None else list2
        return dummy.next


def _build_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def _to_values(node: Optional[ListNode]) -> list[int]:
    values = []
    visited = set()
    while node is not None:
        # A guard makes accidental cycles fail loudly in the local checks.
        assert id(node) not in visited, "cycle detected in merged list"
        visited.add(id(node))
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    cases = [
        ([], []),
        ([], [1]),
        ([1], []),
        ([1, 2, 4], [1, 3, 4]),
        ([-5, -1, 3], [-4, 0, 8]),
        ([1, 1, 1], [1, 1]),
        ([1, 5, 9], [2, 4, 6]),
        ([2, 3, 7], [1, 4, 8]),
        ([-3, -2], [-4, -3]),
        ([0], [0]),
        ([], [-2, 0, 5]),
        ([-10, 0, 10], []),
    ]

    for left, right in cases:
        merged = Solution().mergeTwoLists(_build_list(left), _build_list(right))
        assert _to_values(merged) == sorted(left + right), (left, right)

    print(f"All {len(cases)} regression cases passed.")
