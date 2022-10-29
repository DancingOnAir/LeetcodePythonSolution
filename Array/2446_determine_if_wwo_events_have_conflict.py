from typing import List


class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])

    def haveConflict1(self, event1: List[str], event2: List[str]) -> bool:
        return not (event1[1] < event2[0] or event1[0] > event2[1])


def test_have_conflict():
    solution = Solution()
    assert solution.haveConflict(["01:15", "02:00"], ["02:00", "03:00"])
    assert solution.haveConflict(["01:00", "02:00"], ["01:20", "03:00"])
    assert not solution.haveConflict(["10:00", "11:00"], ["14:00", "15:00"])


if __name__ == '__main__':
    test_have_conflict()
