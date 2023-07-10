class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0
        for x in sentences:
            a = x.count(" ")
            if a + 1 > max:
                max = a + 1
        return max