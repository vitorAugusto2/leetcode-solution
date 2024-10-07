class Solution(object):
    def getLucky(self, s, k):
        num = ""
        for char in s:
            num += str(ord(char) - 96)
        
        while k > 0:
            temp = 0
            for char in num:
                temp += int(char)  
            num = str(temp)  
            k -= 1

        return int(num)  