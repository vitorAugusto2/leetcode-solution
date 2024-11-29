class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for senior in details:
            age = int(senior[11:13])

            if age > 60:
                ans += 1

        return ans

"""
Another Approach
================

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(senior[11:13]) > 60 for senior in details)

* Time Complexity: O(n)
* Space Complexity: O(1)
"""

