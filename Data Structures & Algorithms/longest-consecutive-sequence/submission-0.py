class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = dict()
        longest = 1
        for num in nums:
            length = 1
            pred = num - 1
            succ = num + 1
            if num in seen:
                continue
            elif pred in seen and succ in seen:
                length += seen[pred] + seen[succ]
                seen[pred - seen[pred] + 1] = length
                seen[succ + seen[succ] - 1] = length
            elif pred in seen:
                length += seen[pred]
                seen[pred - seen[pred] + 1] = length
            elif succ in seen:
                length += seen[succ]
                seen[succ + seen[succ] - 1] = length
            if num not in seen:
                seen[num] = length
            #print(seen)
            longest = max(longest,length)
        return longest