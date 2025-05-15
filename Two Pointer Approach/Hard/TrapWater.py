from typing import List
class Solution:

    def trap(self, height: List[int]) -> int:
        ans = 0  # To store the total amount of trapped water
        n = len(height)
        
        # Initialize two pointers at both ends of the array
        l, r = 0, n - 1
        
        # Initialize max heights on both sides
        lmax = rmax = 0
        
        # Traverse the height array using two-pointer technique
        while l < r:
            # Update the maximum height to the left of current position
            lmax = max(lmax, height[l])
            
            # Update the maximum height to the right of current position
            rmax = max(rmax, height[r])
            
            # Water trapped is determined by the shorter side
            if lmax < rmax:
                # Water trapped at position l
                ans += lmax - height[l]
                l += 1
            else:
                # Water trapped at position r
                ans += rmax - height[r]
                r -= 1
        
        return ans  # Return the total trapped water
