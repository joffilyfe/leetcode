class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
        self.index = 0

    def next(self, price: int) -> int:
        self.prices.append(price)

        # index = 2
        # prices = [100, 80, 60, 70]
        # stack = [0, 1, 2]

        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()

        res = self.index + 1 if not self.stack else self.index - self.stack[-1]

        self.stack.append(self.index)
        self.index += 1

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
