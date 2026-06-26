class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0

        for op in operations:
            if op[1] == "+":
                X += 1
            else:
                X -= 1

        return X

# Time Complexity (time:space): O(n) | O(1)

"""

Another Approach
----------------

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(if op[1] == "+" else -1 for op in operations)

# Time Complexity (time:space): O(n) | O(1)
"""
