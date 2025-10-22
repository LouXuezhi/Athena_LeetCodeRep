from collections import defaultdict 

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        demand={}
        # note the char in need
        demandlen=len(t)
        # note the total demanding length
        
        for i in range (len(t)):
            demand[t[i]]=0
        # scan the target string and initialize it
        
        for i in range (len(t)):
            demand[t[i]]+=1
        # scan the target string again and count the amount of the char in demand
        
        lp=-1
        rp=-1
        # initializing the right pointer and the left pointer
        
        critip=(0,float("inf"))
        # when rp do not reach the bounder, the loop will go on
        while (rp<len(s)-1):
             # the first thing to do is to check the status:
             # whether the current window contains the demanded chars are contained
             if (demandlen<=0 ):
                 # this is the situation that the current window contains all the demanded chars
                lp+=1
                # update info
                if demand.get(s[lp])!=None:
                    if demand[s[lp]]==0:
                        # either ==0 or <0
                        # means that the char in window is just the right amount
                        # after deleting, it would be uncomplete again
                        demandlen+=1
                        if rp-lp<critip[1]-critip[0]:
                            critip=(lp,rp)
                    demand[s[lp]]+=1
                 
             else:
                 if (demandlen>0):
                     # this is the situation that the current window do not contain the demanded chars
                     rp+=1
                     # update info
                     if demand.get(s[rp])!= None:
                         if demand[s[rp]] >0:
                             demandlen-=1
                             if demandlen==0 or rp==len(s)-1:
                                 if rp-lp<critip[1]-critip[0]:
                                    critip=(lp,rp)
                         demand[s[rp]]-=1
                     if rp==len(s)-1:
                         while lp<=rp:
                             lp+=1
                             if demand.get(s[lp])!= None:
                                 if demand[s[lp]]==0:
                                     if rp-lp<critip[1]-critip[0]:
                                        critip=(lp,rp)
                                     break
                                 demand[s[lp]]+=1
                                     
                                     
                         
        return s[critip[0]: critip[1]+1]

solution=Solution()
print("********************")
print(solution.minWindow('adobecodebanc','abc'))
print(solution.minWindow('aa','a'))
print("********************")