class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        k = 0

        while l <= r:

            time = 0
            speed = (l + r) // 2

            for pile in piles:
                time += math.ceil(float(pile) / speed)

            if time <= h:
                k = speed
                r = speed - 1
            else:
                l = speed + 1
        
        return k

        