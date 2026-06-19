class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best_count = 0
        cur_count = 0
        for num in nums:
            if num == 1:
                cur_count +=1
            if num == 0:
                if (cur_count > best_count):
                    best_count = cur_count
                cur_count = 0
        if cur_count > best_count:
            best_count = cur_count
        return best_count