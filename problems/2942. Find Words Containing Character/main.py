class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for idx, value in enumerate(words):
            if x in value:
                result.append(idx)
        
        return result