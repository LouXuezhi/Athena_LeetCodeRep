from collections import defaultdict 

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashdict=defaultdict(int)
        sum=0
        count=0
        hashdict[0]=1
        for i in range (len(nums)):
            sum+=nums[i]
            
            count+=hashdict[sum-k]
            hashdict[sum]+=1
               
        return count