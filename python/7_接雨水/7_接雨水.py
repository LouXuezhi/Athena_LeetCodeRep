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

        def get_area(key):
            p=key+1
            rsum=0
            lsum=0
            while height[key]>height[p] :
                if p==length-1:
                    rsum=0
                    break
                rsum+=height[key]-height[p]
                p+=1
            p=key-1 
            while height[key]>height[p] :
                if p==0:
                    lsum=0
                    break
                lsum+=height[key]-height[p]

                p-=1
            return max(rsum,lsum)


        for i in range (length-2):
            dehei.append(height[i]-height[i+1])
        dehei.append(height[length-1])
        for n in range (1,length-2):
            if dehei[n]>0 and dehei[n-1]<=0:
                dichei[n]=height[n]
        for key in sorted(dichei):
            area=get_area(key)
            if area>finalarea:
                finarea=area
        return finalarea


