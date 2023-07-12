class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        list_x = []
        for x in ransomNote:
            if x not in list_x:
                list_x.append(x)
                if magazine.count(x) >= ransomNote.count(x):
                    continue
                else:
                    return False
        return True