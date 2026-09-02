class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        difference = (sum(aliceSizes) - sum(bobSizes)) // 2
        bob_sizes_set = set(bobSizes)
        for alice_candy in aliceSizes:
            bob_candy = alice_candy - difference
            if bob_candy in bob_sizes_set:
                return [alice_candy, bob_candy]
