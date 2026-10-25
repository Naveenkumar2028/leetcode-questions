"""LeetCode 15: 3Sum — O(n^2) time, O(n) sorting space.

Return unique triplets whose sum is zero. Sorting lets us use two pointers
and skip duplicate values without generating duplicate triplets.
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result: List[List[int]] = []

    for i, value in enumerate(nums):
        if value > 0:
            break
        if i > 0 and value == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = value + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([value, nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


if __name__ == "__main__":
    # Lightweight regression checks; run with: python solution.py
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([1, 2, -2, -1]) == []
    assert three_sum([]) == []
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    print("All 3Sum checks passed.")
