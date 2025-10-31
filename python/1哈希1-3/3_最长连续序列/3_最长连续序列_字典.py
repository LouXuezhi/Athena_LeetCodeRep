class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dict={}
        maxlength=0
        
        for n in nums:
            if n not in hash_dict:
                leftlength=hash_dict.get(n-1,0)
                rightlength=hash_dict.get(n+1,0)
                lengthof=leftlength+rightlength+1
                hash_dict[n]=lengthof
                hash_dict[n-leftlength] = lengthof   
                hash_dict[n+rightlength] = lengthof 
                if maxlength<=lengthof:
                    maxlength=lengthof
            
        return maxlength
