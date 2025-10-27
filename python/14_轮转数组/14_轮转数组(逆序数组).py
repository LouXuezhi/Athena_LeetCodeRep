class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums[::]=nums[::-1]
        nums[::]=nums[k-1::-1]+nums[:k-1:-1]
        return nums
    
solution=Solution()
print(solution.rotate([1,2,3,4,5],3))