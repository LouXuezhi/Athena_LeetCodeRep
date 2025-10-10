from collections import defaultdict 

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lengths = len(s) # length of Searched String
        lengthp = len(p) # length of Target String
        lp=0 #left pointer
        rp=0 #right pointer
        ans=[]
        hashdic=defaultdict(int)
        temp=defaultdict(int)
        if lengthp >lengths:
            return []
        for i in range(lengthp):
            hashdic[p[i]]+=1
        while (rp<=lengthp-1):
            temp[s[rp]]+=1
            rp+=1
        if temp==hashdic:
            ans.append(lp)
    
        lp=0
        rp=lengthp-1
        while(rp<lengths-1):
            rp+=1
            temp[s[rp]]+=1 
            lp+=1
            if temp[s[lp-1]]>1:
                temp[s[lp-1]]-=1
            else:
                del temp[s[lp-1]] 
            if temp==hashdic:
                    ans.append(lp)
            

        return ans