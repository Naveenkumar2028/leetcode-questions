class Solution {
    public int longestSubsequence(int[] nums) {
        int xor = 0;
        int zeroCount = 0;

        for (int x : nums) {
            xor ^= x;
            if (x == 0) zeroCount++;
        }

        if (xor != 0) return nums.length;
        if (zeroCount == nums.length) return 0;
        return nums.length - 1;
    }
}