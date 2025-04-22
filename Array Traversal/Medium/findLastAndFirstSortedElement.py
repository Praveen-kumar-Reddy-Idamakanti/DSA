#  binary  Search bcsx Sorted
#  after mid we have two options if tar is mid
#       1-midLeft 2-midRight o
#  other than this we have two options 
#  which is common may be in left or right of mif 
#  so two binary functions for mid 
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findright():
            st=0
            end=len(nums)-1
            index=-1
            while st<=end:
                mid=(st+end)//2
                if nums[mid]==target:
                    index=mid
                    end=mid-1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    st=mid+1
            return index
        def findleft():
            st=0
            end=len(nums)-1
            index=-1
            while st<=end:
                mid=(st+end)//2
                if nums[mid]==target:
                    index=mid
                    st=mid+1
                elif nums[mid]>target:
                    end=mid-1
                else:
                    st=mid+1
            return index

        return [findright(),findleft()]

