from typing import List


# class Solution1:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for idx1,val1 in enumerate(nums):
#             for idx2,val2 in enumerate(nums[idx1+1:]):
#                 if val1+val2 == target:
#                     return [idx1,idx2]


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#             for i in range(len(nums)):
#                 for j in range(i+1,len(nums)):
#                     if nums[i]+nums[j]==target:
#                         return [i,j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for idx,val in enumerate(nums):
            y=target-val
            if y in map:
                return [map[y],idx]
            map[val]=idx
        return []

