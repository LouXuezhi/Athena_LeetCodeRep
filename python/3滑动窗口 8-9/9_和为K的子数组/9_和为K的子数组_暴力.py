class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum=0
        resum=0
        rp=0
        lp=0
        count=0
        
        while(rp<len(nums)and lp<=rp):
            sum+=nums[rp]
            resum=sum
            lp=0
            if resum==k:
                count+=1
            while lp<rp:
                resum-=nums[lp]
                if resum==k:
                    count+=1
                lp+=1
            rp+=1

            
        return count
        
    
# -1 -1 1 -> 0
# 1 -1 0 -> 0
