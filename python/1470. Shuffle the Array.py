class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list_shuffle = []
        i, j = 0, n

        while i < n:
            list_shuffle.append(nums[i])
            list_shuffle.append(nums[j])
            i += 1
            j += 1

        return list_shuffle
