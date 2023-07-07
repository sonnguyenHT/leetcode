class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count = 0
        sub_str = []
        for idx, letter in enumerate(s):
            sub_str.append(letter)
            if count <= 1:
                count = 1
            for j in range(idx+1,len(s)):
                # print(idx,j,sub_str)
                # print(s[j])
                if s[j] not in sub_str:
                    sub_str.append(s[j])
                    if j == len(s) -1 and len(sub_str)> count:
                        count = len(sub_str)
                else :
                    if len(sub_str) > count:
                        count = len(sub_str)
                    # print("count:"+str(count))
                    del sub_str[:]
                    # sub_str.clear() alternate for del command
                    break
            del sub_str[:]
            # sub_str.clear() alternate for del command
        return count