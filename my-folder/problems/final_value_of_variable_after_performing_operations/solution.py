class Solution(object):
    def finalValueAfterOperations(self, operations):
        subtract = 0
        len = 0
        for x in operations:
            if x == "--X" or x == "X--":
                subtract +=1
            len +=1
        return len - 2*subtract