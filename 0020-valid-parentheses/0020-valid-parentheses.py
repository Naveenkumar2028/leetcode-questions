"""LeetCode 20: Valid Parentheses.

Use a stack so each closing bracket must match the most recent opening bracket.
Time complexity: O(n); auxiliary space: O(n).
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []

        for char in s:
            if char in pairs:
                # A closing bracket must match the stack's top.
                if not stack or stack.pop() != pairs[char]:
                    return False
            elif char in "([{":
                stack.append(char)
            else:
                # Defensive handling for characters outside the problem's constraints.
                return False

        # Any leftover opening bracket means the string is incomplete.
        return not stack


if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("(((", False),
        ("]", False),
        ("([{()}])", True),
        ("", True),
        ("abc", False),
        ("(", False),
        (")", False),
    ]

    solution = Solution()
    for value, expected in test_cases:
        actual = solution.isValid(value)
        assert actual == expected, (
            f"isValid({value!r}) returned {actual}; expected {expected}"
        )

    print(f"All {len(test_cases)} Valid Parentheses tests passed.")
