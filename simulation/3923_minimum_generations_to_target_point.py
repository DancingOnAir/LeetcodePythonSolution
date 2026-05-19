class Solution:
    def minGenerations(self, points: list[list[int]], target: list[int]) -> int:
        a1, a2, b1, b2, c1, c2 = 0, 0, 0, 0, 0, 0
        for x in points:
            a1 = min(a1, x[0])
            a2 = max(a2, x[0])
            b1 = min(b1, x[1])
            b2 = max(b2, x[1])
            c1 = min(c1, x[2])
            c2 = max(c2, x[2])

        if not (a1 <= target[0] <= a2 and b1 <= target[1] <= b2 and c1 <= target[2] <= c2) or (len(points) == 1 and target not in points):
            return -1

        if target in points:
            return 0

        res = 0
        seen = set(tuple(p) for p in points)
        while True:
            cur = points[:]
            res += 1
            added = False

            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    if points[i] != points[j]:
                        c = [(points[i][0] + points[j][0]) // 2, (points[i][1] + points[j][1]) // 2, (points[i][2] + points[j][2]) // 2]
                        if c == target:
                            return res
                        if tuple(c) not in seen:
                            seen.add(tuple(c))
                            cur.append(c)
                            added = True
            if not added:
                return -1
            points = cur


def test_min_generations():
    solution = Solution()
    assert solution.minGenerations([[0, 0, 0], [6, 6, 6]], target=[3, 3, 3]) == 1, 'wrong result'
    assert solution.minGenerations([[0, 0, 0], [5, 5, 5]], target=[1, 1, 1]) == 2, 'wrong result'
    assert solution.minGenerations([[0, 0, 0], [2, 2, 2], [3, 3, 3]], target=[2, 2, 2]) == 0, 'wrong result'
    assert solution.minGenerations([[1, 2, 3]], target=[5, 5, 5]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_generations()
