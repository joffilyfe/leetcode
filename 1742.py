class Solution:
    def get_number_sum(self, number: int) -> int:
        total = 0

        while number > 0:
            total += number % 10
            number = number // 10

        return total

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for number in range(lowLimit, highLimit + 1):
            box_number = self.get_number_sum(number)

            if boxes.get(box_number) is None:
                boxes[number] = 0

            boxes[box_number] += 1

        return sorted(boxes.items(), key=lambda x: x[1])[-1][1]


print(Solution().countBalls(lowLimit=1, highLimit=10))
