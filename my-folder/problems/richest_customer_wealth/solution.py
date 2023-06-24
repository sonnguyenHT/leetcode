class Solution(object):
    def maximumWealth(self, accounts):
        return max([sum(acc) for acc in accounts])