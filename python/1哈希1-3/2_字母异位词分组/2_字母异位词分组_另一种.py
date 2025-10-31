class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==1:
            return [strs]
        
        ans={}
        for s in strs:
            sortedstr=str(sorted(s))
            if sortedstr in ans:
                ans[sortedstr].append(s)
            else:
                ans[sortedstr]=[s]
        
        return ans.values()
        
        # sorted 函数
        # sorted(iterable, key=None, reverse=False)
        # string = "python"
        # sorted_string = ''.join(sorted(string))
        # print(sorted_string)  # 输出: hnopty
        # 这里不用 .join 是因为 只做识别不做输出，是否是字符串无所谓

        # dict.values()
        # python 中 返回列表
        # python3 中 需要 list[dict.values()] 才返回列表
        