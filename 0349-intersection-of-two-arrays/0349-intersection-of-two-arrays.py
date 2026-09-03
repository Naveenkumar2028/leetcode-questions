class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        """
        resu = set()

        for x in nums1:
            if x in nums2:
                resu.add(x)
            
     
        return list(resu)
        