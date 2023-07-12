class Solution(object):
    def balancedStringSplit(self, s):
        count_R = 0
        count_L = 0
        count = 0
        for x in s:
            if x == "R":
                count_R += 1
            elif x == "L":
                count_L += 1
            else:
                print("This array is not balance")
                break  
            if count_R == count_L:
                count += 1
                count_R = 0
                count_L = 0
        return count