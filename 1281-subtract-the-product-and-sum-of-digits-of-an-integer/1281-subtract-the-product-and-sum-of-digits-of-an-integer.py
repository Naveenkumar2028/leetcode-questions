class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        prd = 1

        while n >0:
            d = n%10
            prd*=d
            sum+=d
            n//= 10
        
        return prd-sum
        