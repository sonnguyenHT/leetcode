class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for x in jewels:
            count += stones.count(x)    
        return count