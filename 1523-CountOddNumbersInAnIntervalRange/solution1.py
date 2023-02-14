class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = 0

        if high % 2 == 1 or low % 2 == 1:
            odds = ((high-low) // 2) + 1

        else :
            odds = (high - low) // 2

        return odds
