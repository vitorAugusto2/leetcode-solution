class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
        
        return  x == 0 and y == 0
        


"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        
        move_map = {
            "R": (1, 0), 
            "L": (-1, 0), 
            "U": (0, 1), 
            "D": (0, -1)
        }
        
        for move in moves:
            dx, dy = move_map.get(move, (0, 0))
            x += dx
            y += dy
        
        return x == 0 and y == 0
"""
