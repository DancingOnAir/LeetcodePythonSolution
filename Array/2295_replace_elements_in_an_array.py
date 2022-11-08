from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        m = {v: [i] for i, v in enumerate(nums)}
        for a, b in operations:
            if b in m:
                m[b].append(m[a][-1])
            else:
                m[b] = [m[a][-1]]
            m[a].append(-1)

        res = sorted(m.keys(), key=lambda x: m[x][-1])
        return res[-len(nums):]


def test_array_change():
    solution = Solution()
    assert solution.arrayChange([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]]) == [3, 2, 7, 1], 'wrong result'
    assert solution.arrayChange([1, 2], [[1, 3], [2, 1], [3, 2]]) == [2, 1], 'wrong result'


if __name__ == '__main__':
    test_array_change()
