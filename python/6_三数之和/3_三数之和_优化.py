class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range (len(nums)):

            if nums[i]>0:
                return ans
            if i>0 and nums[i]==nums[i-1] :
                continue
            frontp=i+1
            rearp=len(nums)-1
            while (frontp<rearp):

                if nums[frontp]+nums[rearp]+nums[i]==0:
                    ans.append([nums[i],nums[frontp],nums[rearp]])
                    while  nums[frontp]==nums[frontp+1] and frontp<rearp:
                        frontp+=1
                    while nums[rearp]==nums[rearp-1] and frontp<rearp:
                        rearp-=1
                    frontp+=1
                    rearp-=1
                elif nums[frontp]+nums[rearp]+nums[i]<0:
                    frontp+=1
                else:
                    rearp-=1
        
        return ans
