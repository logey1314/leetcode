from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        n=len(height)
        j=n-1
        result=0
        count=0
        while i<n and j<n and i<j:
            c=j-i
            h=min(height[i],height[j])
            count=c*h
            result=max(count,result)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return result

list=[1,8,6,2,5,4,8,3,7]
s=Solution()
print(s.maxArea(list))








