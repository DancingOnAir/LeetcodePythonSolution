from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        return [tomatoSlices // 2 - cheeseSlices, cheeseSlices * 2 - tomatoSlices // 2] if tomatoSlices % 2 == 0 and cheeseSlices * 2 <= tomatoSlices <= cheeseSlices * 4 else []

    def numOfBurgers1(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        diff = tomatoSlices - cheeseSlices * 2
        if tomatoSlices > 4 * cheeseSlices or diff < 0 or diff & 1:
            return []
        return [diff // 2, cheeseSlices - diff // 2]


def test_num_of_burgers():
    solution = Solution()
    assert solution.numOfBurgers(2385088, 164763) == [], 'wrong result'
    assert solution.numOfBurgers(16, 7) == [1, 6], 'wrong result'
    assert solution.numOfBurgers(17, 4) == [], 'wrong result'
    assert solution.numOfBurgers(4, 17) == [], 'wrong result'


if __name__ == '__main__':
    test_num_of_burgers()
