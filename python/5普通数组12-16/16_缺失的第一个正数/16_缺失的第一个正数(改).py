
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums=len(nums)
        for i in range (len_nums):
            if nums[i]<=0:
                nums[i]=len_nums+1
                
        for i in range (len_nums):
            if abs(nums[i])>0 and abs(nums[i])<len_nums+1:
                if nums[nums[i]-1]>0:
                    nums[nums[i]-1]=-nums[nums[i]-1]
                
        for i in range (len_nums):
            if nums[i]>0 :
                return i+1

        return len_nums+1
                