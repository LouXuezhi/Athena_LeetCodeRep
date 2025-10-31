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
        for i in range (count):
            nums.remove(0)
        nums.extend([0]*count)
        
        return nums