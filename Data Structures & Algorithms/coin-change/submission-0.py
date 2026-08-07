class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dptable = [-1] * (amount+1)
        dptable[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if (i - coin >= 0):
                    if (dptable[i - coin] == -1):
                        continue
                    new_amount = dptable[i - coin] + 1
                    if (dptable[i] == -1):
                        dptable[i] = new_amount
                    else:
                        dptable[i] = min(dptable[i],new_amount)
        return dptable[amount]