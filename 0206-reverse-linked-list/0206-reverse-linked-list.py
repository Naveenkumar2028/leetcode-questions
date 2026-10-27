"""LeetCode 206: Reverse Linked List.

Iteratively reverse the next pointers using three references:
previous, current, and next_node.

Time: O(n) | Extra space: O(1)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


def build_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def list_values(head: Optional[ListNode]) -> list[int]:
    values: list[int] = []
    seen: set[int] = set()
    while head is not None:
        node_id = id(head)
        assert node_id not in seen, "cycle detected in linked list"
        seen.add(node_id)
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([0, 0, 0], [0, 0, 0]),
        ([-3, 7, -1], [-1, 7, -3]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        (list(range(100)), list(reversed(range(100)))),
    ]

    solution = Solution()
    for original, expected in cases:
        actual = list_values(solution.reverseList(build_list(original)))
        assert actual == expected, f"{original}: expected {expected}, got {actual}"

    # Verify the implementation relinks the original nodes instead of copying.
    first, second, third = ListNode(1), ListNode(2), ListNode(3)
    first.next, second.next = second, third
    reversed_head = solution.reverseList(first)
    assert reversed_head is third
    assert reversed_head.next is second
    assert reversed_head.next.next is first
    assert reversed_head.next.next.next is None

    print(f"All {len(cases) + 1} reverse-list regression tests passed.")
