class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[::]=matrix[::-1] 
        #return matrix 
        for m in range (len(matrix)):
            for n in range (m,len(matrix)):
                temp=matrix[m][n]
                matrix[m][n]=matrix[n][m]
                matrix[n][m]=temp
        return matrix 
                
                
solution=Solution()
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(solution.rotate(mat))