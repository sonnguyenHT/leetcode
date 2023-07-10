class Solution:
    def interpret(self, command):
        dict = {'G':'G','()':'o','(al)':'al'}
        result = ""
        temp = ""
        for char in command:
            temp += char
            if temp in dict:
                result += dict[temp]
                temp = ""
        return result