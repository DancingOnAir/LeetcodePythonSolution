from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for w in words:
            res.append(chr(ord('z') - sum(weights[ord(c) - ord('a')] for c in w) % 26))
        return ''.join(res)


def test_map_word_weights():
    solution = Solution()
    assert solution.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]) == "rij", 'wrong result'
    assert solution.mapWordWeights(["a","b","c"], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]) == "yyy", 'wrong result'
    assert solution.mapWordWeights(["abcd"], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]) == "g", 'wrong result'


if __name__ == '__main__':
    test_map_word_weights()
