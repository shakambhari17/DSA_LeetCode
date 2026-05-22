class Solution(object):

    def getLucky(self, s, k):

        num = ""

        for ch in s:

            num += str(ord(ch) - ord('a') + 1)

        for i in range(k):

            total = 0

            for digit in num:

                total += int(digit)

            num = str(total)

        return int(num)