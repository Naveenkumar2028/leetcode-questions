class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum = n*(n+1)//2
        actual = 0
        for i in nums:
            actual+=i
        miss = sum - actual
        return miss
        