class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumlist=[[0,0]]
        sum=0
        rp=1
        lp=0
        count=0


        for i in range (len(nums)):
            sum+=nums[i]
            sumlist.append([i+1,sum])
        
        sumlist.sort(key=lambda x: x[1])
        # 不能先排序，会反 sum（1，2） 和 sum （2，1）
        if len(nums)==1 and nums[0]==k:
            return 1
        while(rp<len(sumlist)):
            lp=0
            while (lp<rp):
                if sumlist[rp][1]-sumlist[lp][1]<k:
                    break
                if sumlist[rp][1]-sumlist[lp][1]==k :
                    if sumlist[rp][0]>sumlist[lp][0]:
                        count+=1
                    else:
                        if sumlist[rp][1]==sumlist[lp][1]:
                            count+=1
                if lp ==rp-1:
                    break
                lp+=1


            rp+=1

        return count

#  [-624,-624,-624,-624,-624,-624,-624,-624,-624,-624] 不可行
