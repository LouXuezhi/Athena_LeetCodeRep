class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix) #竖着的高度
        n=len(matrix[0]) #横着的宽度
        wipeh=False
        wipev=False
        for hp in range(n):
            if matrix[0][hp]==0:
                wipeh=True
                break
                
        for vp in range(m):
            if matrix[vp][0]==0:
                wipev=True
                break 
        
        for vp in range(1,m):
            for hp in range (1,n):
                if matrix[vp][hp]==0:
                    matrix[vp][0]=0
                    matrix[0][hp]=0
        # return matrix           
        for hp in range (1,n):
            if matrix[0][hp]==0:
                for vp in range(1,m):
                    matrix[vp][hp]=0
                    
        for vp in range (1,m):
            if matrix[vp][0]==0:
                for hp in range (1,n):
                    matrix[vp][hp]=0
                    
        if wipeh:
            for hp in range(n):
                matrix[0][hp]=0
        if wipev:
            for vp in range (m):
                matrix[vp][0]=0
        return matrix
    
solution=Solution()
mat=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(solution.setZeroes(mat))