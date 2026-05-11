class Solution(object):

    def frequencySort(self, nums):

        freq = {}

        # count frequency
        for num in nums:

            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

        
        nums.sort(key=lambda x: (freq[x], -x))

        return nums