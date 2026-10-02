class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        freqs = Counter(nums) # num : count
        for num, count in freqs.items():
            buckets[count - 1].append(num)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            if len(res) == k:
                break
            else:
                res += buckets[i]
        return res