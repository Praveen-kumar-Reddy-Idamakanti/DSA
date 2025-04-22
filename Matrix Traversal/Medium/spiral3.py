# dx,dy==>dir =[r,d,l,u]
# after 2 dir com step inc
# BC: len(total) < r*c
# x+=dx,y+=dy
# while append in range?(0<=x<row and 0<=y< col)
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[[0,1],[1,0],[0,-1],[-1,0]]# R D L U
        step=1
        x,y=rStart,cStart
        result=[]
        result.append([x,y])
        while len(result)<rows*cols:
            for i in range(4):
                dx,dy=directions[i]
                for _ in range(step):
                    x+=dx
                    y+=dy

                    if 0<=x< rows and 0<=y<  cols:
                        result.append([x,y])
                if i%2==1:
                    step+=1
        return result