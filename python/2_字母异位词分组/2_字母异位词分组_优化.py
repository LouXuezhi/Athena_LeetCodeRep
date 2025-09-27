class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hash(s):
            hashlist=[0]*26
            for i in s:
                hashlist[int(ord(i)-ord('a'))]+=1
            return hashlist
        
        rlist=[]
        found=False
        for s in strs:
            for mem in rlist:
                temp=hash(mem[0])
                for c in s:
                    temp[int(ord(c)-ord('a'))]-=1
                if all (item==0 for item in temp):
                    mem.append(s)
                    found=True
                    break
            if found:
                found=False
                continue
            rlist.append([s]) 
        return rlist

                

            