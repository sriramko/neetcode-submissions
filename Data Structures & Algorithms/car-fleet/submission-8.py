class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        stack = [] # contain times?
        for p, s in cars:
            dist = target - p
            time = dist / s
            if not stack:
                stack.append(time)
            elif p + (stack[-1] * s) < target:
                stack.append(time)
        return len(stack)
