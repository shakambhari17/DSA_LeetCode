class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        
        freq = {}

        for num in arr1:

            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

        result = []

        for num in arr2:

            while freq[num] > 0:

                result.append(num)

                freq[num] -= 1

        for num in sorted(freq):

            while freq[num] > 0:

                result.append(num)

                freq[num] -= 1

        return result