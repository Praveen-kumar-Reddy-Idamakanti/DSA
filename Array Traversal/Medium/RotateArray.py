# first - reverse the array 
# second - reverse the k elements 
# third - reverse the rest of array
# reverse function take three params nums,st,end

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        #reverse the whole list
        self.reverse(nums,0,n-1)
        #revsere the k elements
        self.reverse(nums,0,k-1)
        #reverse the entire elements
        self.reverse(nums,k,n-1)

    def reverse(self,nums,l,r):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        