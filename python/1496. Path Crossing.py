class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = set()
        x = 0
        y = 0

        paths.add((x, y))

        for move in path:
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            elif move == "W":
                x -= 1

            if (x, y) in paths:
                return True

            paths.add((x, y))

        return False

"""
Another Approach
================

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}  
        x, y = 0, 0

        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }

        for move in path:
            dx, dy = moves[move]
            x += dx
            y += dy

            if (x, y) in visited:
                return True
            visited.add((x, y))

        return False

* Time Complexity: O(n)
* Space Complexity: O(n)
"""
