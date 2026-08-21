class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        # Accumulator for the sum of all digits
        total = 0

        # Process each digit from the least significant to the most significant
        while n:
            # Split n into its remaining higher digits (quotient)
            # and the current last digit (remainder)
            n, digit = divmod(n, 10)

            # Add the extracted digit to the running total
            total += digit

        # Return the final digit sum
        return total
