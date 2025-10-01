class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ordernums=sorted(nums)
        length=len(nums)
        ans=[]
        for selectp in range(length):
            demand=0-ordernums.pop(0)
            frontp=0
            rearp=length-2-selectp
            while (frontp<rearp):
                if frontp == -1 or rearp == length-1-selectp:
                    break
                if ordernums[frontp]+ordernums[rearp]<demand:
                    frontp+=1
                    continue
                if ordernums[frontp]+ordernums[rearp]>demand:
                    rearp-=1
                    continue
                if ordernums[frontp]+ordernums[rearp]==demand :
                    partans=sorted([-demand,ordernums[frontp],ordernums[rearp]])
                    if partans not in ans:
                        ans.append(partans)
                    frontp+=1
                    continue
        return ans




