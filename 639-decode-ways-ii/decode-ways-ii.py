class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        prev_prev, prev, curr = 0, 1, 0 
        for i in range(1, n + 1):
            if s[i - 1] == "*":
                curr = (9 * prev) % MOD
            elif s[i - 1] != "0":
                curr = prev
            else:
                curr = 0
            if i > 1:
                if s[i - 2] == "*" and s[i - 1] == "*":
                    curr = (curr + 15 * prev_prev) % MOD
                elif s[i - 2] == "*":
                    if s[i - 1] > "6":
                        curr = (curr + prev_prev) % MOD
                    else:
                        curr = (curr + 2 * prev_prev) % MOD
                elif s[i - 1] == "*":
                    if s[i - 2] == "1":
                        curr = (curr + 9 * prev_prev) % MOD
                    elif s[i - 2] == "2":
                        curr = (curr + 6 * prev_prev) % MOD
                else:
                    if s[i - 2] != "0":
                        two_digit_value = int(s[i - 2]) * 10 + int(s[i - 1])
                        if two_digit_value <= 26:
                            curr = (curr + prev_prev) % MOD
            prev_prev, prev = prev, curr
        return curr
