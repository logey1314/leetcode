
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        record=[]
        if nums is None:
            return []
        n=len(nums)
        nums.sort()

        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    # 和为0，记录下标
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

        return result

s=Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))