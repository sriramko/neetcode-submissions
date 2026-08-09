class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        minimum = n // 3
        res = []
        for num, count in counts.items():
            if count > minimum:
                res.append(num)
        return res