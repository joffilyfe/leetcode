class Solution:
    """This is the brute force solution where we slide the block string for every
    single loop."""
    def minimumRecolors(self, blocks: str, k: int) -> int:
        table = {}

        def nums_of_operations(str):
            return str.count("W")

        minimum_operations = float("inf")

        for i in range(0, len(blocks)):
            substring = blocks[i:i+k]

            if len(substring) == k:
                minimum_operations = min(minimum_operations, nums_of_operations(substring))

        return 0 if minimum_operations == float('inf') else int(minimum_operations)



class OptiomalSolution:
    """The optimal solution uses the sliding window approach to
    increment or decrement the count of W blocks.

    When the window moves right it checks if the leftmost element is W if so remove it from the count
    then check if the current one is W if so increment the count
    """
    def minimumRecolors(self, blocks: str, k: int) -> int:
        with_blocks = blocks[:k].count("W")
        minimum_operations = with_blocks
        left = 0

        for i in range(k, len(blocks)):
            if blocks[left] == 'W':
                with_blocks -= 1

            if blocks[i] == 'W':
                with_blocks += 1

            minimum_operations = min(minimum_operations, with_blocks)
            left += 1



        return minimum_operations if minimum_operations != float('inf') else 0
