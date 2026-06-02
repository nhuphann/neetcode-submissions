class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]

        for i,l in count.items():
            freq[l].append(i)

        res = []

        for x in range(len(freq)-1 ,0 , -1):
            for n in freq[x]:
                res.append(n)
                if len(res) == k:
                    return res
                
                

        

        