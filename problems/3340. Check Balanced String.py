class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_pair = 0
        sum_odd = 0

        for i, digit in enumerate(num):
            if i % 2 == 0:
                sum_pair += int(digit)
            else:
                sum_odd += int(digit)

        return sum_pair == sum_odd
