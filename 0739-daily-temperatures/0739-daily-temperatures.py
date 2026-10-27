"""LeetCode 739: Daily Temperatures.

A monotonic decreasing stack stores indices whose next warmer day is unknown.
Each index is pushed once and popped at most once, giving O(n) time.
Auxiliary space: O(n).
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        waits = [0] * len(temperatures)
        unresolved_days: list[int] = []

        for day, temperature in enumerate(temperatures):
            while (
                unresolved_days
                and temperatures[unresolved_days[-1]] < temperature
            ):
                previous_day = unresolved_days.pop()
                waits[previous_day] = day - previous_day

            unresolved_days.append(day)

        # Days left on the stack have no warmer day, so their answer stays 0.
        return waits


if __name__ == "__main__":
    test_cases = [
        ([], []),
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([60, 50, 40, 30], [0, 0, 0, 0]),
        ([70], [0]),
        ([70, 70, 70], [0, 0, 0]),
        ([70, 71, 70, 72], [1, 2, 1, 0]),
        ([100, 99, 100], [0, 1, 0]),
        ([30, 30, 31, 30, 32], [2, 1, 2, 1, 0]),
        ([50, 60, 55, 65, 40, 70], [1, 2, 1, 2, 1, 0]),
        ([40, 35, 35, 36], [0, 2, 1, 0]),
        ([30, 40, 35, 32, 31, 45], [1, 4, 3, 2, 1, 0]),
    ]

    solver = Solution()
    for temperatures, expected in test_cases:
        actual = solver.dailyTemperatures(temperatures)
        assert actual == expected, (
            f"temperatures={temperatures}: expected {expected}, got {actual}"
        )

    print(f"All {len(test_cases)} regression cases passed.")
