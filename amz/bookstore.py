import heapq
import unittest

"""
CompanyX invests in the success of entrepreneurs, artisans, and small businesses selling in the CompanyX Store. Some of these small businesses are book stores.

CompanyX maintains a portal, where the booksellers can update their inventories. An update received from the portal is
represented by the array updateBook, whose values indicate the following:

1) If updateBook[i] is a positive integer (for example 7), then a copy of the book with book ID updateBook[] is added to the
inventory.
2) If updateBook[i] is a negative integer (for example -11), then a copy of the book with book ID -updateBook[i] (i.e., book ID
11) is removed from the inventory. It is guaranteed that each such update will only be requested if the inventory currently
has at least one copy of that book ID.
3) updateBook[i] is guaranteed to be non-zero.

Given the list of portal updates, the task is to return the maximum copies of any book in the inventory after each update.

Example:

Consider the number of updates to be n = 6, the updates to be updateBook = [6, 6, 2, -6, -2, -6]:
The answer is [1, 2, 2, 1, 1, 0].

Explanation:

The inventory will be updated as follows:
• After the first update, the inventory contains one copy of book ID 6. Maximum copies = 1, of book ID 6
• After the second update, the inventory contains two copies of book ID 6. Maximum copies = 2, of book ID 6
. After the third update, the inventory contains two copies of book ID 6 and one copy of book ID 2. Maximum copies = 2, of book ID 6
• After the fifth update, the inventory contains one copy of book ID 6. Maximum copies = 1, of book ID 6
• After the last update, the inventory is empty. Maximum copies = 0, no books are present.
• After the fourth update, the inventory contains one copy of book ID 6 and one copy of book ID 2. Maximum copies = 1, of Book 6
"""

class Solution:
    def portalUpdate(self, nums=[]):
        table = {}
        result = []
        heap = []

        for number in nums:
            operation = 1 if number > 0 else -1
            number = abs(number)

            table[number] = table.get(number, 0) + operation

            if heap and heap[0][1] == number:
                heapq.heapreplace(heap, (-1 * table[number], number))
            else:
                heapq.heappush(heap, (-1 * table[number], number))

            result.append(heap[0][0] * -1)

        return result



class TestCase(unittest.TestCase):
    def test_first(self):
        self.assertEqual(
            Solution().portalUpdate(nums=[6, 6, 2, -6, -2, -6]), [1, 2, 2, 1, 1, 0]
        )

    def test_second(self):
        self.assertEqual(Solution().portalUpdate(nums=[1, 2, -1, 2]), [1, 1, 1, 2])

    def test_third(self):
        nums = [n for n in range(1, 1_000_000)]
        self.assertEqual(Solution().portalUpdate(nums=nums), [1] * len(nums))


if __name__ == "__main__":
    unittest.main()
