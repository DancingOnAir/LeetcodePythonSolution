from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        return [(i & 1) ^ (c == '(') for i, c in enumerate(seq)]

    def maxDepthAfterSplit1(self, seq: str) -> List[int]:
        res = list()
        cnt = 0

        for c in seq:
            if c == '(':
                cnt += 1
                res += [0] if cnt & 1 else [1]
            else:
                res += [0] if cnt & 1 else [1]
                cnt -= 1
        return res


def test_max_depth_after_split():
    solution = Solution()

    assert solution.maxDepthAfterSplit("(()())") == [0, 1, 1, 1, 1, 0]
    assert solution.maxDepthAfterSplit("()(())()") == [0, 0, 0, 1, 1, 0, 1, 1]


if __name__ == '__main__':
    test_max_depth_after_split()
