import re
import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


paragraph =  "Bob hit a ball, the hit BALL flew far after it was hit."
banned = "hit"

res = Solution().mostCommonWord(paragraph, banned)
print(res)