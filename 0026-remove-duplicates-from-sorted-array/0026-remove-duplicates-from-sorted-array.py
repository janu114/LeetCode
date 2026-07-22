class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = float('-inf')
        k = 0

        for  num in nums:
            if num != prev:
                nums[k]  = num
                prev = num
                k += 1

        return k
        