class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        size = len(str_num)
        totalNums = 0
        i = 0

        # The intuiton was:
        # Loop from 0 to size
        # slice the num as string from i to i + k (k because this sets the size of the number given)
        # Transform the number into int
        # check if the number slice has the size of the k
        #   -> Some times it won't be true because at the last index the str_num size will be _1_
        # check if the number is no 0
        # check if the number is divisible by the slice num as int
        # increase the counter
        while i < size:
            current_num = str_num[i:i+k]

            if len(current_num) == k and int(current_num) != 0 and num % int(current_num) == 0:
                totalNums += 1

            i += 1

        return totalNums
