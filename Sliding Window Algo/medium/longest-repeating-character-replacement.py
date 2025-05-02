class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        res=0
        max_count=0
        count=[0]*26
        for right in range(len(s)):
            idx=ord(s[right])-ord('A')
            count[idx]+=1
            max_count=max(max_count,count[idx])

            window_size=right-left+1
            if window_size -max_count>k:
                count[ord(s[left])-ord('A')]-=1
                left+=1
            res=max(right-left+1,res)
        return res