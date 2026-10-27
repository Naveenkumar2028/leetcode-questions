"""LeetCode 155: Min Stack.

Store each value with the minimum seen at that depth. This makes push, pop,
top, and getMin all O(1) time; the stack uses O(n) extra space.
"""


class MinStack:
    def __init__(self) -> None:
        self._stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, current_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


if __name__ == "__main__":
    checks = 0

    # Negative values and restoring the previous minimum after pop.
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    checks += 1
    stack.pop()
    assert stack.top() == 0 and stack.getMin() == -2
    checks += 1
    stack.pop()
    assert stack.top() == -2 and stack.getMin() == -2
    checks += 1

    # Duplicate minima must remain available after popping one copy.
    stack = MinStack()
    for value in [2, 2, 3, 1, 1, 4]:
        stack.push(value)
    assert stack.getMin() == 1
    checks += 1
    stack.pop()
    assert stack.getMin() == 1
    checks += 1
    stack.pop()
    assert stack.getMin() == 1
    checks += 1
    stack.pop()
    assert stack.top() == 3 and stack.getMin() == 2
    checks += 1
    stack.pop()
    assert stack.top() == 2 and stack.getMin() == 2
    checks += 1

    # Nested negative minima.
    stack = MinStack()
    for value in [-5, -10, -5, -20, -10]:
        stack.push(value)
    assert stack.getMin() == -20
    checks += 1
    stack.pop()
    assert stack.getMin() == -20
    checks += 1
    stack.pop()
    assert stack.getMin() == -10
    checks += 1
    stack.pop()
    assert stack.getMin() == -10
    checks += 1
    stack.pop()
    assert stack.getMin() == -5
    checks += 1

    print(f"All {checks} MinStack regression assertions passed.")
