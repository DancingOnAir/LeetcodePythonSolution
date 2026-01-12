from heapq import heappop, heappush


class Solution:
    def clearStars(self, s: str) -> str:
        hp = []
        for i, c in enumerate(s):
            if c == '*':
                heappop(hp)
            else:
                heappush(hp, (c, -i))
        return ''.join(c for c, _ in sorted(hp, key=lambda x: -x[1]))


def test_clear_stars():
    solution = Solution()
    assert solution.clearStars("aaba*") == "aab", 'wrong result'
    assert solution.clearStars("abc") == "abc", 'wrong result'


if __name__ == '__main__':
    test_clear_stars()
