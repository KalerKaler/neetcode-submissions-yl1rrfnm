class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(cars)[::-1]:

            timeToFinish = (target - p) / s

            if stack and timeToFinish <= stack[-1]:
                continue
            else:
                stack.append(timeToFinish)

        return len(stack)