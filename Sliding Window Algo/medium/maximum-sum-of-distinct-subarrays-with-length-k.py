from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left=0
        max_value=0
        window=set()
        current_sum=0
        
        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                current_sum-=nums[left]
                left+=1
            window.add(nums[right])
            current_sum+=nums[right]
            if right-left+1==k:
                max_value=max(max_value,current_sum)
                window.remove(nums[left])
                current_sum-=nums[left]
                left+=1
        return max_value

            



        