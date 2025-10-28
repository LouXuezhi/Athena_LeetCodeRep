class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        preproduct=[1]
        rearproduct=[1]
        product=1
        ans=[]
        for i in range (len(nums)):
            product*=nums[i]
            preproduct.append(product)
        preproduct.append(1)
        product=1
        for i in range (1,len(nums)+1):
            product*=nums[-i]
            rearproduct.append(product)
        rearproduct.append(1)
        
        for i in range (len(nums)):
            ans.append(preproduct[i]*rearproduct[-3-i])
        return ans

            