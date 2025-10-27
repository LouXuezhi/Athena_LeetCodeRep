class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range (k%len(nums)):
           nums.insert(0,nums.pop())
           
        return nums