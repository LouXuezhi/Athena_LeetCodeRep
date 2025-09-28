class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        maxvalue=max(nums)
        minvalue=min(nums)
        total=0
        ans=0
        hashlist=[False]*(maxvalue-minvalue+1)
        def offset(i):
            return i-minvalue
        for n in nums:
            hashlist[offset(n)]=True

        for n in range(maxvalue-minvalue+1):
            if hashlist[n]:
                total+=1
                
            else:
                if total>=ans:
                    ans=total
                total=0


        return max(total,ans)
    # 第一版，用列表，超出了内存限制


