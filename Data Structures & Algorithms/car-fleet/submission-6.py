class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)
        stack = [] # contain times?
        num = len(cars)
        for p, s in cars:
            dist = target - p
            time = dist / s
            if len(stack) == 0:
                stack.append(time)
                continue
            if p + (stack[-1] * s) >= target:
                num -= 1
                continue
            stack.append(time)
        return num
