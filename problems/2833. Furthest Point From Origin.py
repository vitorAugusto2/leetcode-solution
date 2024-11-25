class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        moves_freq = Counter(moves)

        return abs(moves_freq["L"] - moves_freq["R"]) + moves_freq["_"]