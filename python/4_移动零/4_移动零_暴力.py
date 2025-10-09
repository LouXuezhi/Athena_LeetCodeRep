class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        for n in nums :
            if n==0:
                count+=1
                nums.remove(0)
                nums.append(0)
        return nums