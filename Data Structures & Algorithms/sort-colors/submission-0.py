class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        j = len(nums) - 1
        count = 0
        tmp = nums[:]

        for i, n in enumerate(tmp):
            if n == 0:
                nums[k] = n
                k += 1
            elif n == 2:
                nums[j] = n
                j -= 1
            else:
                count += 1
        
        nums[k:j+1] = [1] * count

            








# 1 0 1 2




# 1 0 1 2



