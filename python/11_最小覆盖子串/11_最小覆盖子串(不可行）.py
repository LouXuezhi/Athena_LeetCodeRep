from collections import defaultdict 

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        demand={}
        demandlen=len(t)
        minpos=(0,float("inf"))

        lp=0
        rp=0
        for i in range (len(t)):
            demand[t[i]]=0
        for i in range (len(t)):
            demand[t[i]]+=1

        for n,c in enumerate(s):
            if demand.get(c,None)!=None:
                if demand[c]>0:
                    demandlen-=1
                demand[c]-=1

            if demandlen==0:
                while(lp<n):
                    if demand.get(s[lp],None)!=None:
                        if demand[s[lp]]>=0:
                            demandlen+=1
                            break
                        demand[s[lp]]+=1
                    lp+=1

            if (minpos[1]-minpos[0])>n-lp:
                    minpos=(lp,n)

        return s[minpos[0]:minpos[1]+1]
                    

