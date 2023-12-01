from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        expected_index_quantities = {}
        counts = defaultdict(lambda: 0)

        for i, n in enumerate(num):
            expected_index_quantities[i] = int(n)

            if counts.get(int(n)) is None:
                counts[int(n)] = 1
            else:
                counts[int(n)] += 1

        for number, expected in expected_index_quantities.items():
            if expected == counts.get(number, 0):
                continue
            else:
                return False

        return True


print(Solution().digitCount(num="1210"))
