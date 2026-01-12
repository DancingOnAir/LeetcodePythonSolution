class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(int(x) * (-1 if i & 1 else 1) for i, x in enumerate(num)) == 0


def test_is_balanced():
    solution = Solution()
    assert not solution.isBalanced("1234"), 'wrong result'
    assert solution.isBalanced("24123"), 'wrong result'


if __name__ == '__main__':
    test_is_balanced()
