class Solution(object):
    def minPartitions(self, n):
        x = "9"
        while x not in n:
            x = str(int(x) - 1)
        return int(x)