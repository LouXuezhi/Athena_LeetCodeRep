from collections import defaultdict


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=defaultdict(int)
        minv=float('inf')
        temp=0
        for i in range (len(nums)):
            if nums[i]>0 and ans[nums[i]]==0:
                ans[nums[i]]+=1
        
        if ans[1]==0:
            return 1
                
        for key in ans.keys():
            if ans[key]>=1 and ans[key+1]==0:
                temp=key+1
                if minv>temp:
                    minv=temp
                
        return minv
                
                    