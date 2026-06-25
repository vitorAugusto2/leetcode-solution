class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ids = []

        for id in order:
            if id in friends:
                ids.append(id)

        return ids

# Time Complexity (time:space): O(n) | O(n+m) or O(n)


"""
Another Approach
----------------

# 1 - List Comprehension
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        return [id for id in order if id in friends]

# Time Complexity (time:space): O(n) | O(n+m) or O(n)

# 2 - Hash
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ids = []
        friends_set = set(friends)

        for id in order:
            if id in friends:
                ids.append(id)

        return ids

# Time Complexity (time:space): O(n) | O(n+m) or O(n)
"""
