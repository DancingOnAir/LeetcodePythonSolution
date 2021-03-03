from typing import List
from collections import Counter


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        transpose_items = list(zip(*items))
        rule_keys = {'type': 0, 'color': 1, 'name': 2}
        counter = Counter(transpose_items[rule_keys[ruleKey]])

        return counter[ruleValue]


def test_count_matches():
    solution = Solution()

    items1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey1 = "color"
    ruleValue1 = "silver"
    assert solution.countMatches(items1, ruleKey1, ruleValue1) == 1, 'wrong result'

    items2 = [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]]
    ruleKey2 = "type"
    ruleValue2 = "phone"
    assert solution.countMatches(items2, ruleKey2, ruleValue2) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_matches()
