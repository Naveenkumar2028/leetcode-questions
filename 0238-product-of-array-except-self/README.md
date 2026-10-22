# 238. Product of Array Except Self

## Approach: prefix and suffix products

For each index, the result is the product of all values to its left multiplied by the product of all values to its right. The solution makes two passes and does not use division.

1. In the left-to-right pass, store the running product of values before each index.
2. In the right-to-left pass, multiply each result by the running product of values after that index.

The running products start at `1`, so the approach naturally handles zeros without special cases.

## Complexity

- **Time:** O(n), with two passes through the array.
- **Auxiliary space:** O(1), excluding the output array.

## Run the tests

From the repository root, compile the solution and standalone test harness:

```sh
javac 0238-product-of-array-except-self/0238-product-of-array-except-self.java 0238-product-of-array-except-self/ProductOfArrayExceptSelfTest.java
java -cp 0238-product-of-array-except-self ProductOfArrayExceptSelfTest
```

The test harness checks normal input, zeros, negative values, and a two-element array.
