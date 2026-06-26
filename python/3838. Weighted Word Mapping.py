class Solution:
    def mapWordWeights(self, words, weights):
        ans = []

        for word in words:
            total = 0
            for char in word:
                total += weights[ord(char) - ord("a")]
            ans.append(chr(ord("z") - total % 26))

        return "".join(ans)

# Time complexity (time:space): O(n) | O(1)
