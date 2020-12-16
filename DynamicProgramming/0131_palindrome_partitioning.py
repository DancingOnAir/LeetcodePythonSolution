from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = list()
        

        return res


def test_partition():
    solution = Solution()
    assert solution.partition('aab') == [["a", "a", "b"], ["aa", "b"]], 'wrong result'
    assert solution.partition('a') == [["a"]], 'wrong result'


if __name__ == '__main__':
    test_partition()
