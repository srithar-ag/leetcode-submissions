class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        from typing import List
from functools import cache
from itertools import accumulate
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        """
        Stone Game V: Alice and Bob play a game with stones in a row.
        Each turn, a player divides stones into two non-empty groups.
        The player with smaller sum gets points equal to that sum.
        If sums are equal, player chooses which sum to take as points.
        Returns maximum points Alice can get with optimal play.
        """
      
        @cache
        def dp(left: int, right: int) -> int:
            if left >= right:
                return 0
          
            max_score = 0
            left_sum = 0
            right_sum = prefix_sum[right + 1] - prefix_sum[left]
            for split_point in range(left, right):
                left_sum += stoneValue[split_point]
                right_sum -= stoneValue[split_point]
              
                if left_sum < right_sum:
                    if max_score >= left_sum * 2:
                        continue
                    max_score = max(max_score, left_sum + dp(left, split_point))
                elif left_sum > right_sum:
                    if max_score >= right_sum * 2:
                        break
                    max_score = max(max_score, right_sum + dp(split_point + 1, right))
                else:
                    max_score = max(
                        max_score,
                        max(left_sum + dp(left, split_point), 
                            right_sum + dp(split_point + 1, right))
                    )
            return max_score
        prefix_sum = list(accumulate(stoneValue, initial=0))
        return dp(0, len(stoneValue) - 1)
