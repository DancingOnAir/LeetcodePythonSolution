from bisect import bisect_right


cnt = {}
MX = 10 ** 9
a = 1
while a ** 3 * 2 <= MX:
    b = a
    tot = a ** 3 + b ** 3
    while tot <= MX:
        cnt[tot] = cnt.get(tot, 0) + 1
        b += 1
        tot = a ** 3 + b ** 3
    a += 1

goods = sorted(k for k, v in cnt.items() if v > 1)


class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        i = bisect_right(goods, n)
        return goods[:i]


def test_find_good_integers():
    solution = Solution()
    assert solution.findGoodIntegers(4104) == [1729,4104], 'wrong result'
    assert solution.findGoodIntegers(578) == [], 'wrong result'


if __name__ == '__main__':
    test_find_good_integers()
