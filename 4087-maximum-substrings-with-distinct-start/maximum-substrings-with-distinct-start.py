class Solution:
    def maxDistinct(self, s: str) -> int:
        unique_chars = set(s)
        return len(unique_chars)