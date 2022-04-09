class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        maxIndex = nums.index(max_num)
        nums.remove(max_num)
        for idx, x in enumerate(nums):
            if x*2 > max_num:
                return -1
        return maxIndex
