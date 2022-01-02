class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        m = mass
        for n in asteroids:
            if m >= n:
                m = m + n
            else:
                return False
        return True