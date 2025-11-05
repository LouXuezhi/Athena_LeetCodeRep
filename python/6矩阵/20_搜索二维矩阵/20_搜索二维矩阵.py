class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m= len(matrix)
        n= len(matrix[0])
        
        position=[m-1,0]
        
        while (True):
            if (position[0]<0 or position[1]<0 or position[0]>m-1 or position[1]>n-1):
                return False
            if matrix[position[0]][position[1]]==target:
                return True
            else:
                if matrix[position[0]][position[1]]>target:
                    position[0]-=1
                if matrix[position[0]][position[1]]<target:
                    position[1]+=1
                    
                    
solution=Solution()
mat=[[-1,3]]
print(solution.searchMatrix(mat,3))    