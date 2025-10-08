class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        words = title.split()

        for word in words:
            if len(word) <= 2:
                ans.append(word.lower())
            else:
                ans.append(word.capitalize())

        return " ".join(ans)