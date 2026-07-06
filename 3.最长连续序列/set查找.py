from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result=1
        count = 1
        if not nums:
            return 0

        hash_set=set(nums)
        for number in hash_set:
            if number -1 in hash_set:
                continue
            count=1
            num=number
            while(num +1 in hash_set ):
                count=count+1
                num=num+1
                result=max(count,result)

        result=result=max(count,result)


        return  result
