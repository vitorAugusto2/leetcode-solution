class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"\w+", paragraph.lower())
        filtered_words = [word for word in words if word not in set(banned)]
        word_count = Counter(filtered_words)

        return word_count.most_common(1)[0][0]
