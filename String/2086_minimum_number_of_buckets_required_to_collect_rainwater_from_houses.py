class Solution:
    def minimumBuckets(self, street: str) -> int:
        if street == 'H' or street.startswith('HH') or street.endswith('HH') or 'HHH' in street:
            return -1
        return street.count('H') - street.count('H.H')


def test_minimum_buckets():
    solution = Solution()
    assert solution.minimumBuckets("H..H") == 2, 'wrong result'
    assert solution.minimumBuckets(".H.H.") == 1, 'wrong result'
    assert solution.minimumBuckets(".HHH.") == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_buckets()
