class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_of_nums=len(nums)
        for i in range (len_of_nums):
            ith_num=nums[i]
            for n in range (i+1,len_of_nums):
                if (ith_num+nums[n]==target):
                    return [i,n]
#暴力算法，注意Range范围 range（a, b,c ）a取得到，b 取不到 c为步长
#1905ms