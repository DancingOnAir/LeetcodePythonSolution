class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        cnt = 0
        i = p1 = p2 = 0
        for a, b in zip(s, goal):
            if a != b:
                cnt += 1
                if cnt == 1:
                    p1 = i
                elif cnt == 2:
                    p2 = i
                elif cnt > 2:
                    return False
            i += 1
        if not cnt:
            return len(set(s)) < len(s)
        return s[p1] == goal[p2] and s[p2] == goal[p1]


def test_buddy_strings():
    solution = Solution()
    assert solution.buddyStrings("acccccb", "bccccca"), 'wrong result'
    assert solution.buddyStrings('ab', 'ba'), 'wrong result'
    assert not solution.buddyStrings('ab', 'ab'), 'wrong result'
    assert solution.buddyStrings('aa', 'aa'), 'wrong result'


if __name__ == '__main__':
    test_buddy_strings()
