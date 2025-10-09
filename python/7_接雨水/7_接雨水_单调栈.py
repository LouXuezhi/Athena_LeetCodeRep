class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        class Sdstack:
            def __init__(self ):
                self.stacklist=[]

            def add(self,mem):
                self.stacklist.append(mem)
                
            def len (self):
                return len(self.stacklist)
            
            def curntlast(self):
                return int(self.stacklist[-1])
                
            def pop(self):
                if len(self.stacklist)>0:
                    return self.stacklist.pop()
                else :
                    return False
                
            def iflenge2(self):
                if len(self.stacklist)>=2:
                    return True
                else:
                    return False

            def iflenge1(self):
                if len(self.stacklist)>=1:
                    return True
                else:
                    return False   

        sdstack=Sdstack()
        sdstack.add(0)
        totalsum=0
        if height is None :
            return 0
        for n in range (1,len(height)):
            while  sdstack.iflenge1():
                if height[n]<height[sdstack.curntlast()]:
                    sdstack.add(n)
                    break
                else:
                    popped=sdstack.pop()
                    if sdstack.iflenge1() :
                        totalsum+=(n-sdstack.curntlast()-1)*(min(height[n],height[sdstack.curntlast()])
                                                    -height[popped])
                    else:
                        sdstack.add(n)
                        break
                    

        return totalsum
                    
                



                
