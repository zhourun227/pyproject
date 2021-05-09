from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            if i==0:
                nums[i]=nums[i]
            else:
                nums[i]=nums[i]+nums[i-1]
        return nums




s=Solution()
l=s.runningSum([1,2,3,4])
print(l)