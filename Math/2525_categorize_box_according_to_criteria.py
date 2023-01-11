class Solution:
    # Bulky    Heavy    idx         bits    string
    # –––––    ––––––   –––––––     ––––    –––––––
    # False    False    0+0 = 1     00      Neither
    # True     False    1+0 = 1     01      Bulky
    # False    True     0+2 = 2     10      Heavy
    # True     True     1+2 = 3     11      Both
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        idx = int(length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10 ** 9) + 2 * (mass >= 100)
        return ("Neither", "Bulky", "Heavy", "Both")[idx]

    def categorizeBox1(self, length: int, width: int, height: int, mass: int) -> str:
        def helper(arr):
            return [a >= 10 ** 4 for a in arr]

        res1 = any(helper([length, width, height])) or length * width * height >= 10 ** 9
        res2 = mass >= 100

        if res1 and res2:
            return "Both"
        elif res1:
            return "Bulky"
        elif res2:
            return "Heavy"
        return "Neither"


def test_categorize_box():
    solution = Solution()
    assert solution.categorizeBox(1000, 35, 700, 300) == "Heavy", 'wrong result'
    assert solution.categorizeBox(200, 50, 800, 50) == "Neither", 'wrong result'


if __name__ == '__main__':
    test_categorize_box()
