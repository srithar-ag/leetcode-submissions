class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def can_alice_win(count: List[int]) -> bool:
            if count[1] == 0:
                return False
            count[1] -= 1
            total_moves = 1 + min(count[1], count[2]) * 2 + count[0]
            if count[1] > count[2]:
                count[1] -= 1
                total_moves += 1
            return total_moves % 2 == 1 and count[1] != count[2]
        remainder_count = [0] * 3
        for stone in stones:
            remainder_count[stone % 3] += 1
        strategy_one = [remainder_count[0], remainder_count[1], remainder_count[2]]
        strategy_two = [remainder_count[0], remainder_count[2], remainder_count[1]]
        return can_alice_win(strategy_one) or can_alice_win(strategy_two)
