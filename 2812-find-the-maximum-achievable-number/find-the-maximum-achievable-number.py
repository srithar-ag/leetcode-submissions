class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        """
        Calculate the maximum achievable value of x.
      
        In each operation, we can either:
        - Increase num by 1 and decrease x by 1, OR
        - Decrease num by 1 and increase x by 1
      
        After t operations, the maximum x occurs when we always increase num,
        which means x can be at most num + 2*t (since each operation increases
        the gap between num and x by 2).
      
        Args:
            num: The starting integer value
            t: The number of operations allowed
          
        Returns:
            The maximum achievable value of x after t operations
        """
        # Each operation can increase the difference between num and x by 2
        # So the maximum achievable x is num plus twice the number of operations
        return num + t * 2
