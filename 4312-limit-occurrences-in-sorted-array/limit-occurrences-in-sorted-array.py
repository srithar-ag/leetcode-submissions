from typing import List


class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        # Total number of elements in the input list
        n = len(nums)
        count = write_index = 1
        for read_index in range(1, n):
            if nums[read_index] != nums[read_index - 1]:
                count = 1
            else:
                count += 1
            if count <= k:
                nums[write_index] = nums[read_index]
                write_index += 1
        return nums[:write_index]
