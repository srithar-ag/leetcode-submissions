class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0   # XOR of all elements in nums
        zero_count = 0  # number of zeros in nums

        # Compute the XOR of the whole array and count zeros in one pass
        for num in nums:
            total_xor ^= num
            zero_count += int(num == 0)

        # Case 1: XOR of all elements is non-zero,
        # so the entire array is a valid subsequence
        if total_xor:
            return n

        # Case 2: every element is zero,
        # so no subsequence can have a non-zero XOR
        if zero_count == n:
            return 0

        # Case 3: total XOR is zero but at least one element is non-zero.
        # Removing one non-zero element makes the remaining XOR non-zero,
        # so the answer is n - 1
        return n - 1
