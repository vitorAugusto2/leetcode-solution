class Solution:
    def romanToInt(self, s: str) -> int:
        dict_num_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and dict_num_roman[s[i]] < dict_num_roman[s[i + 1]]:
                ans -= dict_num_roman[s[i]]
            else:
                ans += dict_num_roman[s[i]]

        return ans

"""
Another Approach
----------------

class Solution:
    def romanToInt(self, s: str) -> int:
        dict_num_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0
        prev_value = 0

        for char in s[::-1]:
            curr_value = dict_num_roman[char]
            if curr_value < prev_value:
                ans -= curr_value
            else:
                ans += curr_value
            prev_value = curr_value

        return ans
        
# Time Complexity: O(n) | O(n)

"""