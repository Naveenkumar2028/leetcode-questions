class Solution:
    def longestSubsequence(self, nums):
        xor = 0
        all_zero = True

        for num in nums:
            xor ^= num
            if num != 0:
                all_zero = False

        if xor != 0:
            return len(nums)

        if all_zero:
            return 0

        return len(nums) - 1