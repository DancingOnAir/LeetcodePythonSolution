from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        end = [x for x in freq if x % 2 == 0]

        res = set()
        for x in end:
            cur = x
            freq[x] -= 1
            for y, v1 in freq.items():
                if v1 > 0:
                    cur += y * 10
                    freq[y] -= 1
                    for z, v2 in freq.items():
                        if z and v2 > 0:
                            cur += z * 100
                            res.add(cur)
                            cur -= z * 100
                    freq[y] += 1
                    cur -= y * 10
            freq[x] += 1
        return sorted(res)


def test_find_even_numbers():
    solution = Solution()

    assert solution.findEvenNumbers([2, 1, 3, 0]) == [102, 120, 130, 132, 210, 230, 302, 310, 312, 320], 'wrong result'
    assert solution.findEvenNumbers([2, 2, 8, 8, 2]) == [222, 228, 282, 288, 822, 828, 882], 'wrong result'
    assert solution.findEvenNumbers([3, 7, 5]) == [], 'wrong result'
    assert solution.findEvenNumbers([0, 2, 0, 0]) == [200], 'wrong result'
    assert solution.findEvenNumbers([0, 0, 0]) == [], 'wrong result'


if __name__ == '__main__':
    test_find_even_numbers()
