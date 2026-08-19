class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        max_k_value = float('-inf')
        stack = []
        for current_num in reversed(nums):
            if current_num < max_k_value:
                return True
            while stack and stack[-1] < current_num:
                max_k_value = stack.pop()
            stack.append(current_num)
        return False
