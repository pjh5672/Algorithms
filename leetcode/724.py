class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        leftsum = 0
        for idx, x in enumerate(nums):
            if leftsum == (S-leftsum-x):
                return idx
            leftsum += x
        return -1
            