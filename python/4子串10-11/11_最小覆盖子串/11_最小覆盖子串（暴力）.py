from collections import defaultdict 

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        shashdict= defaultdict(int)
        thashdict = defaultdict(int)
        lp=0
        rp=0
        note=[]
        ans=[]
        minlen=0
        minindex=0

        for c in range(len(t)):
            thashdict[t[c]]+=1

        for i in range(len(s)):
            if thashdict[s[i]]>=1:
                note.append([i,s[i]])

        thashdict.clear()
        for c in range(len(t)):
            thashdict[t[c]]+=1 

        for i in range(len(note)):
            shashdict.clear()
            rp=i
            lp=i
            while(rp<len(note)):
                if shashdict[note[rp][1]]<thashdict[note[rp][1]]:
                    shashdict[note[rp][1]]+=1
                if thashdict==shashdict:
                    ans.append([note[lp][0],note[rp][0],note[rp][0]-note[lp][0]+1])
                    break
                rp+=1

        if ans != []:
            minlen=ans[0][2]
        else:
            return ""

        for i in range (len(ans)):
            if minlen>=ans[i][2]:
                minlen=ans[i][2]
                minindex=i

        return s[ans[minindex][0]:ans[minindex][1]+1]
            

            



        