import re
import collections

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        strs: Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
