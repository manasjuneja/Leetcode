class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mapped_list = map(sum, accounts)
        return max(mapped_list)

