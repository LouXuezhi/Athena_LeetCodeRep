class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lmaxlist=[]
        rmaxlist=[]
        lmax=0
        rmax=len(height)-1
        area=0
        if len(height)<3:
            return 0
        for n in range (len(height)):
            if height[n]>=height[lmax]:
                lmax=n
            lmaxlist.append(lmax)
        
        for n in range (len(height)-1,-1,-1):
            if height[n]>=height[rmax]:
                rmax=n
            rmaxlist.append(rmax)

        for n in range (1,len(height)-1,1):
            incre=(min (height[lmaxlist[n]],height[rmaxlist[len(height)-n-1]])-height[n])
            if incre>=0:
                area+=incre

        return area

