import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]

res = Solution().groupAnagrams(strs)
print(res)