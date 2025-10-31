from pydoc import tempfilepager


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x : x[0])
        ans=[]

        
        while (len(intervals)>0):
            temp=intervals[0]
            while (True):
                if intervals[0][0]<=temp[1]:
                    temp[1]=max(temp[1],intervals[0][1])
                    intervals.pop(0)
                    if len(intervals)==0:
                       ans.append(temp) 
                       break
                else:
                    ans.append(temp)
                    break
                
            
                    
        return ans
                