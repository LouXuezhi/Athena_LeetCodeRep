
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash_map={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if compliment in hash_map:
                return [hash_map[compliment],i]
            else:
                hash_map[nums[i]]=i
        return []
    # 注意过程意识 
    # 即边检测是否符合条件边更新hash表，而不是先全部注册完hash表在遍历一遍检测
    # hash表用字典比列表更灵活
    # 用好 in 字典查询不到值会报错而不是返回None