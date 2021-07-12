from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        memo = [i for i, c in enumerate(boxes) if c == '1']
        res = list()
        for i, c in enumerate(boxes):
            cur = 0
            for j in memo:
                cur += abs(j - i)
            res.append(cur)
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations('110') == [1, 1, 3], 'wrong result'
    assert solution.minOperations('001011') == [11, 8, 5, 4, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_min_operations()
