class Solution(object):

    def groupAnagrams(self, strs):
                            
        totaltable = {}
    
        def checkif(s, cmpstr):
                                # early length check
            if len(s) != len(cmpstr):
                return False
            temp = dict(totaltable[cmpstr])
                                # subtract characters from the candidate string `s`
            for ch in s:
                temp[ch] -= 1
                                # verify all counts returned to zero
            for k in range(26):
                if temp[chr(ord('a') + k)] != 0:
                    return False
            return True

        def maketable(s):
            totaltable[s] = {chr(ord('a') + i): 0 for i in range(26)}
            for ch in s:
                totaltable[s][ch] += 1


        rlist = []
        for s in strs:
            found = False
            for grp in rlist:
                if checkif(s, grp[0]):
                    grp.append(s)
                    found = True
                    break
            if found:
                continue
            rlist.append([s])
            maketable(s)
        return rlist

        # 改进： 每次都要建立哈希表-> 建立映射表