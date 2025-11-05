class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        count=0
        while (m>0 and n>0):
            if count%4==0:
                for i in range(n):
                    ans.append(matrix[0].pop(0))
                matrix.pop(0)
                m-=1
                    
            if count%4==1:
                for i in range (m):
                    ans.append(matrix[i].pop(-1))
                n-=1
                    
            if count%4==2:
                for i in range (n):
                    ans.append(matrix[-1].pop(-1))
                matrix.pop(-1)
                m-=1
                    
            if count%4==3:
                for i in range (m):
                    ans.append(matrix[-i-1].pop(0))
                n-=1
            
            count+=1
        
        return ans
    
    
solution=Solution()
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(mat))