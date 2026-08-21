from typing import List


class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        # The degree of each vertex equals the sum of its row in the adjacency matrix
        return [sum(row) for row in matrix]
