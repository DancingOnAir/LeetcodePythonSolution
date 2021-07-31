from typing import List


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        mutated = False
        for i, c in enumerate(num):
            cur = int(c)
            if cur < change[cur]:
                mutated = True
                num[i] = str(change[cur])
            elif cur > change[cur] and mutated:
                break
        return ''.join(num)

    def maximumNumber1(self, num: str, change: List[int]) -> str:
        res = list(num)
        for i, c in enumerate(num):
            cur = int(c)
            if cur < change[cur]:
                res[i] = str(change[cur])
                j = i + 1
                while j < len(num) and int(num[j]) <= change[int(num[j])]:
                    res[j] = str(change[int(num[j])])
                    j += 1
                break
        return ''.join(res)


def test_maximum_number():
    solution = Solution()
    assert solution.maximumNumber("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832", 'wrong result'
    assert solution.maximumNumber("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == "934", 'wrong result'
    assert solution.maximumNumber("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == "5", 'wrong result'


if __name__ == '__main__':
    test_maximum_number()

