# matrix size -->n
# inserting positon by incrementing num 
# same as spiral 1
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        top,bottom=0,n-1
        left,right=0,n-1
        num=1
        while left<=right and top<=bottom:
            
            #left-->right
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1

            for i in range(top,bottom+1):
                matrix[i][right]=num
                num+=1
            right-=1
            
            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num+=1
            bottom-=1

            for i in range(bottom,top-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1

        return matrix

            