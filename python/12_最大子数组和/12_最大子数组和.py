class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp=[nums[0]]
        
        for i in range (len(nums)-1):
            dp.append(max(nums[i+1],dp[i]+nums[i+1]))
            
        return max(dp)
        
            
            
            
            