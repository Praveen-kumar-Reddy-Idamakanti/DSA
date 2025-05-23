# prefix calculate 
# suffix calculate 
# them multiply them for except element
from typing import List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        result=[0]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]

        for i in range(n):
            result[i]=prefix[i]*suffix[i]
        return result