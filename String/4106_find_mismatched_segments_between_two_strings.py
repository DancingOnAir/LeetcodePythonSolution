class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        res = []
        n = len(s1)
        start = 0
        for i in range(n):
            if s1[i] == s2[i]:
                start = i + 1
            elif i == n - 1 or s1[i + 1] == s2[i + 1]:
                res.append([s1[start: i+1], s2[start: i+1]])
        return res


def test_find_mismatched_segments():
    solution = Solution()
    assert solution.findMismatchedSegments("earth", s2 = "empty") == [["ar","mp"],["h","y"]]
    assert solution.findMismatchedSegments("action", s2 = "nation") == [["ac","na"]]
    assert solution.findMismatchedSegments("hot", s2 = "hot") == []


if __name__ == '__main__':
    test_find_mismatched_segments()
