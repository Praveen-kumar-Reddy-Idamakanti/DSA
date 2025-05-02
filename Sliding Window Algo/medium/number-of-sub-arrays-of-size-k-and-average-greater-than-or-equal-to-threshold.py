from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        counter=0
        window=sum(arr[:k])
        if window//k >=threshold:
            counter+=1
        for right in range(k,len(arr)):
            window-=arr[left]
            left+=1
            window+=arr[right]
            if window//k >=threshold:
                counter+=1
        return counter
            


