class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k=k%len(nums)
        if k==0:
            return nums
        temp=nums[-k:]
        for i in range(k):
            nums.pop()
        temp.extend(nums)
        nums[::]=temp
        return nums
    
solution=Solution()
print(solution.rotate([1],0))