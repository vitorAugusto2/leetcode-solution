class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        for i in range(len(matrix)):
            degree = 0
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    degree += 1
            ans.append(degree)

        return ans

# Time Complexity: O(n2) | O(n)

"""
Another solution
----------------

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]

# Time Complexity: O(n2) | O(n)
"""
