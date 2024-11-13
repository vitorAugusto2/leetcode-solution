class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        s1, s2 = Counter(ransomNote), Counter(magazine)
        return s1 & s2 == s1