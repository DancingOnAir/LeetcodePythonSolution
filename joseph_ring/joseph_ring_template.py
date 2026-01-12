# Joseph Ring: https://blog.csdn.net/tingyun_say/article/details/52343897
class JosephRing:
    # n个人, 每次选第m个人，下标为0开始
    def joseph_ring_top_down(self, n, m):
        if n == 1:
            return 0
        return (self.joseph_ring_top_down(n - 1, m) + m) % n

    def joseph_ring_bottom_up(self, n, m):
        res = 0
        for i in range(2, n+1):
            res = (res + m) % i

        return res


def test_joseph_ring():
    solution = JosephRing()
    assert solution.joseph_ring_top_down(5, 3) == 3, 'wrong result'
    assert solution.joseph_ring_top_down(10, 17) == 2, 'wrong result'

    assert solution.joseph_ring_bottom_up(5, 3) == 3, 'wrong result'
    assert solution.joseph_ring_bottom_up(10, 17) == 2, 'wrong result'


if __name__ == "__main__":
    test_joseph_ring()
