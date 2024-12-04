class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()

        if len(pattern) != len(s_split):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for p, word in zip(pattern, s_split):
            if p not in pattern_to_word:
                if word in word_to_pattern:
                    return False
                pattern_to_word[p] = word
                word_to_pattern[word] = p
            elif pattern_to_word[p] != word:
                return False

        return True


sol = Solution()
print(sol.wordPattern("abba", "dog dog dog dog"))  # False