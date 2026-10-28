"""LeetCode 150: Evaluate Reverse Polish Notation.

Use a stack: operands are pushed, and each operator consumes the last two
operands. Division truncates toward zero, as required by the problem.

Time: O(n) | Auxiliary space: O(n)
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                # Avoid float conversion so large integers remain exact.
                quotient = abs(left) // abs(right)
                if (left < 0) != (right < 0):
                    quotient = -quotient
                stack.append(quotient)

        return stack[-1]


if __name__ == "__main__":
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
            22,
        ),
        (["7", "-3", "/"], -2),
        (["-7", "3", "/"], -2),
        (["7", "3", "/"], 2),
        (["-7", "-3", "/"], 2),
        (["3", "4", "-"], -1),
        (["2", "3", "*", "5", "+"], 11),
    ]

    solver = Solution()
    for tokens, expected in test_cases:
        actual = solver.evalRPN(tokens)
        assert actual == expected, (
            f"tokens={tokens}: expected {expected}, got {actual}"
        )

    print(f"All {len(test_cases)} Evaluate Reverse Polish Notation cases passed.")
