class Solution:
    # Binary Indexed Tree
    def minMovesToMakePalindrome(self, s: str) -> int:
        pass

    # greedy
    def minMovesToMakePalindrome1(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1:
                res += i // 2
            else:
                res += i
                s.pop(i)
            s.pop()

        return res


def test_min_moves_to_make_palindrome():
    solution = Solution()
    assert solution.minMovesToMakePalindrome("aabb") == 2, 'wrong result'
    assert solution.minMovesToMakePalindrome("letelt") == 2, 'wrong result'


if __name__ == '__main__':
    test_min_moves_to_make_palindrome()
