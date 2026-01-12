class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(c) - 96) for c in s)

        for i in range(k):
            s = str(sum(int(c) for c in s))
        return int(s)


def test_get_lucky():
    solution = Solution()
    assert solution.getLucky('iiii', 1) == 36, 'wrong result'
    assert solution.getLucky('leetcode', 2) == 6, 'wrong result'
    assert solution.getLucky('zbax', 2) == 8, 'wrong result'


if __name__ == '__main__':
    test_get_lucky()
