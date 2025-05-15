from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list to make it easier to avoid duplicates and use two-pointer technique
        nums = sorted(nums)
        ans = []

        # Iterate through the list, treating nums[i] as the first element of the triplet
        for i in range(len(nums)):
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers: one just after i, and one at the end
            k = i + 1
            l = len(nums) - 1

            # Use the two-pointer approach to find pairs that, with nums[i], sum to 0
            while k < l:
                total = nums[i] + nums[k] + nums[l]

                # If the triplet sums to 0, add it to the result
                if total == 0:
                    ans.append([nums[i], nums[k], nums[l]])

                    # Move both pointers to look for next possible pair
                    k += 1
                    l -= 1

                    # Skip duplicates for the second number
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1

                    # Skip duplicates for the third number
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

                # If the total is more than 0, move right pointer left to reduce sum
                elif total > 0:
                    l -= 1

                # If the total is less than 0, move left pointer right to increase sum
                else:
                    k += 1

        # Return the list of unique triplets
        return ans
