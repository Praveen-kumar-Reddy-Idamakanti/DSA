from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m=len(p)
        n=len(s)
        ans=[]
        if m>n:
            return []
        count_p=Counter(p)
        window=Counter(s[:m])
        if window==count_p:
            ans.append(0)
         
        for right in range(m,n):
            window[s[right]]+=1
            window[s[right-m]]-=1
            if window[s[right-m]]==0:
                del window[s[right-m]]
            if window==count_p:
                ans.append(right-m+1)
        return ans

