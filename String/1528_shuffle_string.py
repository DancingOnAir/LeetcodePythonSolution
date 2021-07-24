from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        memo = [[indices[i], s[i]] for i in range(len(s))]
        memo.sort(key=lambda x: x[0])
        return ''.join(memo[i][1] for i in range(len(s)))


def test_restore_string():
    solution = Solution()
    assert solution.restoreString('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]) == 'leetcode', 'wrong result'
    assert solution.restoreString('abc', [0, 1, 2]) == 'abc', 'wrong result'
    assert solution.restoreString('aiohn', [3, 1, 4, 2, 0]) == 'nihao', 'wrong result'
    assert solution.restoreString('aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5]) == 'arigatou', 'wrong result'
    assert solution.restoreString('art', [1, 0, 2]) == 'rat', 'wrong result'


if __name__ == '__main__':
    test_restore_string()
