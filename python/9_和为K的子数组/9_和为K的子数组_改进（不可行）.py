class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumtable=[0]
        sum=0
        rp=1
        lp=0
        count=0


        for i in range (len(nums)):
            sum+=nums[i]
            sumtable.append(sum)
        sumtable.sort()
        # 不能先排序，会反 sum（1，2） 和 sum （2，1）
        while(rp<len(sumtable)):

            while (lp<rp):

                if sumtable[rp]-sumtable[lp]<k:
                    break
                if sumtable[rp]-sumtable[lp]==k:
                    count+=1
                if (lp<rp-1):
                    lp+=1
                else:
                    break


            rp+=1

        return count




