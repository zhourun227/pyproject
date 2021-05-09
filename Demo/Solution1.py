from typing import List, Set


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s= Set[int]
        for i in range(nums):
            s.add(i)
        return s.size()!=nums.__len__()

s=Solution1()
print(s)