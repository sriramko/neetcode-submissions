class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already = set()
        for num in nums:
            if num in already: 
                return True
            already.add(num)
        return False
        
        