class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        asteroids.sort()
        for i, x in enumerate(asteroids):
            if mass < x:
                return False
            mass += x
            if mass >= asteroids[-1]:
                return True
        return True


def test_asteroid_destroyed():
    solution = Solution()
    assert solution.asteroidsDestroyed(10, asteroids=[3, 9, 19, 5, 21]), 'wrong result'
    assert not solution.asteroidsDestroyed(5, asteroids=[4, 9, 23, 4]), 'wrong result'


if __name__ == '__main__':
    test_asteroid_destroyed()
