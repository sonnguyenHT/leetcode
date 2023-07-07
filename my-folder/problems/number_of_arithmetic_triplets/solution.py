class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        dic = {} # store nums[i]
        quest = {} # store require number you possible find after nums[i]
        count = 0 # count answer
        for i in nums:
            dic[i] = True 
            if i in quest: count += 1 # meet demand 
            if i - diff in dic: quest[i + diff] = True
        print(dic)
        print(quest)
        return count 