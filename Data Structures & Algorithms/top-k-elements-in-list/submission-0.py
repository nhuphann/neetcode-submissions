class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        # 1. count frequency
        for n in nums:
            count[n] += 1

        # 2. sort by frequency
        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # 3. take top k
        return sorted_nums[:k]