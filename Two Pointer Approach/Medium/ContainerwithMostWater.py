from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers at the start and end of the height list
        i = 0
        j = len(height) - 1
        
        # Variable to store the maximum area found
        area = 0

        # Loop until the two pointers meet
        while i < j:
            # Width of the container is the distance between the two pointers
            width = j - i
            
            # Height of the container is the minimum of the two heights
            min_height = min(height[i], height[j]) 
            
            # Calculate the area and update max area if it's greater
            area = max(area, min_height * width)
            
            # Move the pointer with the smaller height inward
            # (We do this because moving the taller one cannot increase area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        # Return the maximum area found
        return area
