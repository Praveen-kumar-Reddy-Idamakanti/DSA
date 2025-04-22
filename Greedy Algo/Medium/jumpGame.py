# greedy algorithm
# fartest varialble tracks reached end or beyond that
# if index crosses fartest False
# we will update the varible in sucha a way that if max of far,i+nums[i]


from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            # If we are at an index that is not reachable, return False
            if i > farthest:
                return False
            
            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or exceed the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        return False
