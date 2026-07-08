class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        if len(s)==1:
            return 1
        n=len(s)
        i=0
        j=1
        result=0
        t=set(s[i])
        while i<=j and i<n and j<n:
            if  j<n and s[j] not in t :
                t.add(s[j])
                result=max(result,len(t))
                j=j+1
            elif i<n and s[j] in t:
                result=max(result,len(t))
                t.remove(s[i])
                i=i+1

        return result

s=Solution()
print(s.lengthOfLongestSubstring(""))
