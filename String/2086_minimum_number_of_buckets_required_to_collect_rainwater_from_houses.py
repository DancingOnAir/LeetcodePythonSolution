class Solution:
    # greedy
    def minimumBuckets1(self, street: str) -> int:
        if street == 'H' or street.startswith('HH') or street.endswith('HH') or 'HHH' in street:
            return -1
        return street.count('H') - street.count('H.H')

    # dp
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        res = 0
        for i, val in enumerate(street):
            if val == 'H':
                if i > 0 and street[i - 1] == 'B':
                    continue
                elif i < len(street) - 1 and street[i + 1] == '.':
                    res += 1
                    street[i + 1] = 'B'
                elif i > 0 and street[i - 1] == '.':
                    res += 1
                    street[i - 1] = 'B'
                else:
                    return -1
        return res


def test_minimum_buckets():
    solution = Solution()
    assert solution.minimumBuckets("H..H") == 2, 'wrong result'
    assert solution.minimumBuckets(".H.H.") == 1, 'wrong result'
    assert solution.minimumBuckets(".HHH.") == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_buckets()
