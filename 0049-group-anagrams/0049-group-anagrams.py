class Solution(object):

    def groupAnagrams(self, strs):

        hashmap = {}

        for word in strs:

            sorted_word = "".join(sorted(word))

            if sorted_word not in hashmap:

                hashmap[sorted_word] = []

            hashmap[sorted_word].append(word)

        return hashmap.values()