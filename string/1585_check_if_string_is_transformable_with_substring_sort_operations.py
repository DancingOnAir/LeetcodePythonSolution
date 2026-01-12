from collections import Counter, deque


class Solution:
    # https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/discuss/843917/C%2B%2BJavaPython-O(n)
    def isTransformable(self, s: str, t: str) -> bool:
        pos = {i: deque() for i in range(10)}
        for i, c in enumerate(s):
            pos[int(c)].append(i)

        for i, c in enumerate(t):
            digit = int(c)
            if not pos[digit]:
                return False
            if any(pos[j] and pos[j][0] < pos[digit][0] for j in range(digit)):
                return False
            pos[digit].popleft()
        return True


def test_is_transformable():
    solution = Solution()
    assert solution.isTransformable('84532', '34852'), 'wrong result'
    assert solution.isTransformable('34521', '23415'), 'wrong result'
    assert not solution.isTransformable('12345', '12435'), 'wrong result'
    assert not solution.isTransformable('1', '2'), 'wrong result'
    assert not solution.isTransformable('12', '21'), 'wrong result'


if __name__ == '__main__':
    test_is_transformable()
