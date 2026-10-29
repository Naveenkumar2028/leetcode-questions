"""LeetCode 238: Product of Array Except Self.

Uses prefix and suffix products so division is not required.
Time: O(n). Extra space: O(1), excluding the returned output list.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i, value in enumerate(nums):
            result[i] = prefix
            prefix *= value

        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([0, 0], [0, 0]),
        ([0, 4, 0], [0, 0, 0]),
        ([2, -3, 4, -5], [60, -40, 30, -24]),
        ([1, 1], [1, 1]),
        ([7], [1]),
        ([], []),
    ]

    solution = Solution()
    for nums, expected in cases:
        original = nums.copy()
        actual = solution.productExceptSelf(nums)
        assert actual == expected, (
            f"nums={nums}: expected {expected}, got {actual}"
        )
        assert nums == original, "The input list must not be modified."

    print(f"All {len(cases)} regression tests passed.")
