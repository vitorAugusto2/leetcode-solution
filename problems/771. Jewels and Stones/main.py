class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        qte_stones = 0
        
        for i in stones:
            if i in jewels:
                qte_stones += 1
        
        return qte_stones