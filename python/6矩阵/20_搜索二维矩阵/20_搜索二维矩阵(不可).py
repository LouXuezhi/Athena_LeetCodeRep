class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        v=-1
        
        n=len(matrix[0])
        h=-1
        sumh=0
        sumv=0
        s=min(m,n)
        sign=False
        if target >matrix[m-1][n-1] or target<matrix[0][0]:
            return False
        else:
            #print("else")
            if m>=n:
                #print("m>=n")
                if n==1:
                    h=0
                    v=0
                    sign=True
                    
                while ((n+sumv)<=m):
                    #print("in loop")
                    if matrix[s+sumv-1][s-1]==target:
                        #print("matrix[s+sumv-1][s-1]==target")
                        return True
                    if matrix[sumv+s-1][s-1]>target:
                        if n==1:
                            h=0
                            v=0
                            sign=True
                        else:
                        #print("matrix[s+sumv-1][s-1]>target") 
                            for i in range (s-1):
                                if matrix[sumv+i][i]==target:
                                #print("matrix[sumv+i][i]==target")
                                    return True
                                if matrix[sumv+i][i]<target and matrix[sumv+i+1][i+1]>target:
                                #print("GET!m>=n")
                                    h=i
                                    v=sumv+i
                                    sign=True
                                    break
                    if matrix[s+sumv-1][s-1]<target:
                        #print("matrix[s+sumv-1][s-1]<target") 
                        if sumv==0:
                            return False
                        if(sumv+s>m):
                            sumv=m-n
                            sign=True
                        else:
                            sumv+=s
                            sumv+=s
                            continue  
                    if sign==True:
                        break
                    
            if m<n:
                if m==1:
                    h=0
                    v=0
                    sign=True
                while (s+sumv<=n):
                    if matrix[s-1][s+sumh-1]==target:
                        #print('matrix[s-1][s+sumh-1]==target')
                        return True
                    if matrix[s-1][s+sumh-1]>target:
                        #print('matrix[s-1][s+sumh-1]>=target')
                        if m==1:
                            h=0
                            v=0
                            sign=True
                            break
                        else:
                            for i in range (s-1):
                                if matrix[i][i]==target:
                                #print('matrix[i][i]==target')
                                    return True
                                if matrix[i][i]<target and matrix[i+1][i+1]>target:
                                #print('Get') 
                                    v=i
                                    h=sumh+i
                                    sign=True
                                    break
                    if matrix[s-1][s+sumh-1]<target:
                        #print("matrix[s-1][s+sumh-1]<target")
                        if sumv==0:
                            return False
                        if(sumh+s>n):
                            sumv=n-m
                            sign=True
                        else:
                            sumh+=s
                            continue  
                    if sign==True:
                        break
        if h<0 or v<0:
            #print("h|v<0")
            return False
        for i in range(m):
            if matrix[i][h] == 0:
                return True
        for i in range (n):
            if matrix[v][i] == 0:
                return True
            
            return False       
                    
                    
    
solution=Solution()
mat=[[-1,3]]
print(solution.searchMatrix(mat,3))    