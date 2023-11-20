from collections import deque


class Solution:
    # deque
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        if start.replace('_', '') != target.replace('_', ''):
            return False

        left = deque()
        right = deque()
        for i, c in enumerate(start):
            if c == 'L':
                left.append(i)
            elif c == 'R':
                right.append(i)

        for i, c in enumerate(target):
            if c == 'L':
                if i > left.popleft():
                    return False
            elif c == 'R':
                if i < right.popleft():
                    return False

        return True

    # brute force
    def canChange1(self, start: str, target: str) -> bool:
        i, j, n = 0, 0, len(start)

        while i < n and j < n:
            while i < n and start[i] == '_':
                i += 1

            if i >= n:
                break

            if start[i] == 'L':
                while j < n and target[j] != 'L':
                    if target[j] == 'R':
                        return False
                    j += 1

                if j > i or j == n:
                    return False
            elif start[i] == 'R':
                while j < n and target[j] != 'R':
                    if target[j] == 'L':
                        return False
                    j += 1

                if j < i or j == n:
                    return False
            i += 1
            j += 1

        while i < n:
            if start[i] != '_':
                return False
            i += 1

        while j < n:
            if target[j] != '_':
                return False
            j += 1

        return True


def test_can_change():
    solution = Solution()
    assert not solution.canChange("R", "_"), 'wrong result'
    assert solution.canChange("_L__R__R_", "L______RR"), 'wrong result'
    assert not solution.canChange("R_L_", "__LR"), 'wrong result'
    assert not solution.canChange("_R", "R_"), 'wrong result'


if __name__ == '__main__':
    test_can_change()
