class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
    
        dehei=[]
        dichei={}
        length=len(height)
        finalarea=0

        def get_larea(key):
            lsum=0
            p=key-1 
            while height[key]>height[p] :
                if p==0:
                    lsum=0
                    break
                lsum+=height[key]-height[p]

                p-=1
            return lsum
        def get_rarea(key):
            p=key+1
            rsum=0
            while height[key]>height[p] :
                if p==length-1:
                    rsum=0
                    break
                rsum+=height[key]-height[p]
                p+=1
            p=key-1  
            return rsum
        def get_area(key):
            
            return max(get_larea(key),get_rarea(key))

        for i in range (1,length-1):
            if ((height[i-1]<=height[i] and height[i+1]<height[i] ) 
                or(height[i-1]<height[i] and height[i+1]<=height[i] )):
                area=get_area(i)
                finalarea+=area
        finalarea+=(get_rarea(0)+get_larea(length-1))
        return finalarea
# 算成了最大面积而非总面积