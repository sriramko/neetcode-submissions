class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1): return nums[0]
        profit = [[0,0] for _ in range(n)] #[max w/ #1,max w/o #1]
        profit[0][0] = nums[0]
        profit[0][1] = 0
        profit[1][0] = nums[0]
        profit[1][1] = nums[1]
        for i in range(2,n):
            if (i == (n-1)):
                profit[i][0] = profit[i-1][0]
            else:
                profit[i][0] = max(profit[i-1][0],(nums[i]+profit[i-2][0]))
            profit[i][1] = max(profit[i-1][1],(nums[i]+profit[i-2][1]))
        return max(profit[n-1][0],profit[n-1][1])
