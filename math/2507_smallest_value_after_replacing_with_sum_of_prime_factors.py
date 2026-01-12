class Solution:
    def smallestValue(self, n: int) -> int:
        def prime(num):
            s = 0
            for i in range(2, int(n ** 0.5) + 1):
                while num % i == 0:
                    s += i
                    num //= i
            if num > 1:
                s += num
            return s

        while True:
            res = prime(n)
            if res == n:
                break
            n = res
        return res

    def smallestValue1(self, n: int) -> int:
        cur, res = n, 0
        for i in range(2, n + 1):
            while cur % i == 0:
                res += i
                cur //= i
        return res if res == n else self.smallestValue(res)


def test_smallest_value():
    solution = Solution()
    assert solution.smallestValue(15) == 5, 'wrong result'
    assert solution.smallestValue(3) == 3, 'wrong result'


if __name__ == '__main__':
    test_smallest_value()
