class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            dp[0][j] = j
        for i, char1 in enumerate(word1, 1):
            dp[i][0] = i
            for j, char2 in enumerate(word2, 1):
                if char1 == char2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[m][n]
