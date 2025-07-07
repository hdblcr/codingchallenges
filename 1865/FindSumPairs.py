import collections
class FindSumPairs:
# LeetCode Daily Question 7/6/2025

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = collections.Counter(nums2)
        print("counter: ", self.counter)

    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        _nums1, _counter  = self.nums1, self.counter
        countTotals = 0
        for num in _nums1:
            #  Check if tot - num (index of the value in hash map) exists
            if (diff := tot - num) in _counter:
                countTotals += _counter[diff]
        return countTotals

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
