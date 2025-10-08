from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed)   
        count = 0

        for word in words:
            if set(word) <= set_allowed:
                print(word)
                count += 1


        return count


sol = Solution()
print(sol.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))