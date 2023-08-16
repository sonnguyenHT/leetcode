class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            dict_a = dict()
            dict_b = dict()
            for x in s:
                if x not in dict_a:
                    dict_a[x] = 1
                else:
                    dict_a[x] += 1 
            for y in t:
                if y not in dict_b:
                    dict_b[y] = 1
                else:
                    dict_b[y] += 1 
            for x in dict_a:
                if x not in dict_b:
                    return False
                elif dict_a[x] != dict_b[x]:
                    return False
        return True