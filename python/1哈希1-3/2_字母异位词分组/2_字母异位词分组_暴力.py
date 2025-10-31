class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def checkif (str,cmpstr):
            if len(str)==len(cmpstr):
                map={chr(ord('a')+i):0 for i in range (26)}
                for i in range (len(str)):
                    map[str[i]]+=1
                for n in range (len(str)):
                    map[cmpstr[n]]-=1
                for k in range (26):
                    if not map[chr(ord('a')+k)]==0:
                        return False
                    
            else:
                return False
            return True

        rlist=[]
        SignPost=False
        for str in strs:
            for cmp in rlist:
                if checkif (str,cmp[0]):
                    cmp.append(str)
                    SignPost=True
                    break
            if SignPost:
                SignPost = False
                continue
            rlist.append([str])

        return rlist

           # 未通过：超时 但逻辑正确 