from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements={}
        for i in range(len(nums)):
            if (target-nums[i]) not in complements:
                complements[nums[i]]=i
            else:
                return [complements[target-nums[i]],i]

test = Solution()
print("[2,7,11,15], 9 = ", test.twoSum([2,7,11,15], 9))
print("[3,2,4], 6 = ", test.twoSum([3,2,4], 6))
print("[3,3], 6 = ", test.twoSum([3,3], 6))
