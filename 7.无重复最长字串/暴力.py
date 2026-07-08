class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        if len(s)==1:
            return 1
        n=len(s)
        result=0
        for i in range(0,n):
            count=1
            for j in range(i+1,n):
                if s[j] not in s[i:j]:
                    count=count+1
                    result=max(count,result)
                else:
                    result = max(count, result)
                    break


        return result

s=Solution()
print(s.lengthOfLongestSubstring("bbbb"))
