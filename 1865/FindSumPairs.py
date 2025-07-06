class FindSumPairs:
# LeetCode Daily Question 7/6/2025

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.instructions = nums1
        self.nums1 = nums1
        self.nums2 = nums2
        self.output = []
        for i in range(len(nums1)):
            self.output.append([])
        

    def add(self, index: int, val: int) -> None:
        self.nums2[index] = self.nums2[index] + val

    def count(self, tot: int) -> int:
        countTotals = 0
        print('self.nums1: ', self.nums1, '\n')
        print('self.nums2: ', self.nums2)
        for index1 in range(len(self.nums1)):
            for index2 in range(len(self.nums2)):
                if self.nums1[index1] + self.nums2[index2] == tot:
                    countTotals = countTotals + 1
        return countTotals

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
