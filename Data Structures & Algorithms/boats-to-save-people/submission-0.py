class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boat = 0
        while left <= right:
            remaining = limit - people[right]
            right -= 1
            boat += 1
            if people[left] <= remaining and left <= right:
                left += 1
        return boat