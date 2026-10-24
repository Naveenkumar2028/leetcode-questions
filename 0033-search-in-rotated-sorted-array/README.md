# 33. Search in Rotated Sorted Array

**Difficulty:** Medium · **Technique:** Modified binary search  
**Time:** O(log n) · **Extra space:** O(1)

## Approach
A sorted array rotated at an unknown pivot still has at least one sorted half in every search interval (assuming distinct values).

1. Compute the midpoint as `left + (right - left) / 2`.
2. Return the midpoint if it matches the target.
3. If the left half is sorted, search it only when the target falls in its range; otherwise search the right half.
4. If the right half is sorted, search it only when the target falls in its range; otherwise search the left half.
5. Return `-1` if the target is absent.

Duplicate values are outside the problem's constraints and can make the sorted half ambiguous.

## Run checks
From the repository root:

```sh
javac 0033-search-in-rotated-sorted-array/Solution.java 0033-search-in-rotated-sorted-array/SearchInRotatedSortedArrayTest.java
java -cp 0033-search-in-rotated-sorted-array SearchInRotatedSortedArrayTest
```
