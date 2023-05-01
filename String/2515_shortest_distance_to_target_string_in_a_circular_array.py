from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = 0
        while res < n:
            if words[(startIndex + res) % len(words)] == target or words[(startIndex - res) % len(words)] == target:
                return res
            res += 1
        return -1


def test_closet_target():
    solution = Solution()
    assert solution.closetTarget(["hello", "i", "am", "leetcode", "hello"], "hello", 1) == 1, 'wrong result'
    assert solution.closetTarget(["a", "b", "leetcode"], "leetcode", 0) == 1, 'wrong result'


if __name__ == '__main__':
    test_closet_target()
