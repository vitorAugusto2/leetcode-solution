"""
Approach
--------

1. Converting the letter to a number (ah -> 1-8)
2. If the sum is even, the square is black; if the sum is odd, the square is white.
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        convert_column = ord(coordinates[0]) - ord("a") + 1
        row = int(coordinates[1])
    
        return (convert_column + row) % 2 == 1