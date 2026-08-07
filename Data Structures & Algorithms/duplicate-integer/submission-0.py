class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already = []
        for num in nums:
            if (num in already): 
                return True
            else:
                already.append(num)
        return False
        
        