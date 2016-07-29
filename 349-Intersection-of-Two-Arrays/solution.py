class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_set1 = set(nums1)
        num_set2 = set(nums2)
        return list(num_set1 & num_set2)
            