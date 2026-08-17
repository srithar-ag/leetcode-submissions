class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        from typing import List
from itertools import count

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        consecutive_sum = nums[0]
        index = 1
        while index < len(nums) and nums[index] == nums[index - 1] + 1:
            consecutive_sum += nums[index]
            index += 1
        seen_numbers = set(nums)
        for candidate in count(consecutive_sum):
            if candidate not in seen_numbers:
                return candidate
