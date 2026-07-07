from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        n=len(nums)
        while i<n and j<n :
            if i<n  and nums[i] != 0 :
                i=i+1
            if j<n  and nums[j]==0:
                j=j+1
            if i<n and j<n and i<=j:
                nums[i],nums[j]=nums[j],nums[i]

            j=j+1

nums=[1,0,1]
sou=Solution()
sou.moveZeroes(nums)
print(nums)