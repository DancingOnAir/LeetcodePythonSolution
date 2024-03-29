from typing import List


class Solution:
    # https://leetcode.com/problems/replace-elements-in-an-array/solutions/2112285/python-simple-map-approach/
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        replace = dict()
        for a, b in reversed(operations):
            replace[a] = replace.get(b, b)
        for i, val in enumerate(nums):
            if val in replace:
                nums[i] = replace[val]
        return nums

    def arrayChange2(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        m = {v: i for i, v in enumerate(nums)}
        for a, b in operations:
            m[b] = m[a]
            nums[m[a]] = b
        return nums

    def arrayChange1(self, nums: List[int], operations: List[List[int]]) -> List[int]:
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
