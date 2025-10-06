class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length=len(height)
        height.append(0)
        rmaxlog=[-1]*length
        lmaxlog=[-1]*length
        area=0

        for i in range (length):
            for n in range (i+1,length):
                if height[n]>height[i] and height[n]>height[rmaxlog[i]]:
                    rmaxlog[i]=n
                    
   
            for n in range (i-1,-1,-1):
                if height [n]>height[i]and height[n]>=height[lmaxlog[i]]:
                    lmaxlog[i]=n
                
        
        for i in range (length):
            if lmaxlog[i]>=0 and rmaxlog[i]>=0:
                area+=(min(height[rmaxlog[i]],height[lmaxlog[i]])-height[i])

        return area



            
