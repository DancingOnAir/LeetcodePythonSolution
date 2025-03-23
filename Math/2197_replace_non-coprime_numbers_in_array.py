from typing import List
from math import gcd


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            while res:
                g = gcd(res[-1], x)
                if g > 1:
                    x *= res.pop() // g
                else:
                    break
            res.append(x)
        return res


def test_replace_non_coprimes():
    solution = Solution()
    assert solution.replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]) == [12, 7, 6], 'wrong result'
    assert solution.replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3]) == [2, 1, 1, 3], 'wrong result'


if __name__ == '__main__':
    test_replace_non_coprimes()
