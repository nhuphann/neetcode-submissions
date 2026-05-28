class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(list)

        for i, n in enumerate(nums):
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
        
        return max(dict, key=dict.get)


