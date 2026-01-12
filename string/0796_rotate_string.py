class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

    def rotateString1(self, s: str, goal: str) -> bool:
        return any((s[i:] + s[:i]) == goal for i in range(len(s)))


def test_rotate_string():
    solution = Solution()
    assert solution.rotateString("abcde", "cdeab"), 'wrong result'
    assert not solution.rotateString("abcde", "abced"), 'wrong result'


if __name__ == '__main__':
    test_rotate_string()
