from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = keysPressed[0]
        max_duration = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration:
                max_duration = duration
                res = keysPressed[i]
            elif duration == max_duration and keysPressed[i] > res:
                res = keysPressed[i]
        return res


def test_slowest_key():
    solution = Solution()

    releaseTimes1 = [9, 29, 49, 50]
    keysPressed1 = "cbcd"
    assert solution.slowestKey(releaseTimes1, keysPressed1) == 'c', "wrong result"

    releaseTimes2 = [12, 23, 36, 46, 62]
    keysPressed2 = "spuda"
    assert solution.slowestKey(releaseTimes2, keysPressed2) == 'a', "wrong result"


if __name__ == '__main__':
    test_slowest_key()
