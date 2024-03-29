from itertools import combinations


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(first, second, s):
            if first != str(int(first)) and second != str(int(second)):
                return False
            if not s:
                return True

            total = str(int(first) + int(second))
            return s.startswith(total) and dfs(second, total, s[len(total):])

        return any(dfs(num[:i], num[i:j], num[j:]) for i, j in combinations(range(1, len(num)), 2))

    def isAdditiveNumber1(self, num: str) -> bool:
        n = len(num)

        def dfs(first, second, s):
            if not s:
                return True

            total = first + second
            if s.startswith(str(total)):
                return dfs(second, total, s[len(str(total)):])
            return False

        for i in range(1, n - 1):
            if num[0] == '0' and i > 1:
                break
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break
                if dfs(int(num[:i]), int(num[i:j]), num[j:]):
                    return True

        return False


def test_is_additive_number():
    solution = Solution()
    assert solution.isAdditiveNumber("112358"), 'wrong result'
    assert solution.isAdditiveNumber("199100199"), 'wrong result'


if __name__ == '__main__':
    test_is_additive_number()
