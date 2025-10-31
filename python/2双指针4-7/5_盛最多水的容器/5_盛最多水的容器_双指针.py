class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftp=0
        rightp=len(height)-1
        maxarea=0
        while (leftp<rightp):
            area=(rightp-leftp)*min(height[leftp],height[rightp])
            if area>maxarea:
                maxarea=area
            if height[leftp]<height[rightp]:
                leftp+=1
            else:
                rightp-=1
        return maxarea
