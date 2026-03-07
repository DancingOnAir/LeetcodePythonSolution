from typing import List


class Solution:
    def toggleLightBulbs(self, bulbs: List[int]) -> List[int]:
        cnt = [0] * 101
        for i in bulbs:
            cnt[i] += 1
        return [i for i, x in enumerate(cnt) if x & 1]


def test_toggle_light_bulbs():
    solution = Solution()
    assert solution.toggleLightBulbs([10, 30, 20, 10]) == [20, 30], 'wrong result'
    assert solution.toggleLightBulbs([100, 100]) == [], 'wrong result'


if __name__ == '__main__':
    test_toggle_light_bulbs()
