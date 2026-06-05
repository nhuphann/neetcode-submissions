class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        
        freq = [[] for _ in range(len(nums) + 1)]

        for x, c in count.items():
            freq[c].append(x)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res




