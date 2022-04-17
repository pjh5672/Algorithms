# 234. Palindrome Linked List

import collections

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        q = collections.deque()

        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

if __name__ == "__main__":
    a = [1, 2, 2, 1]
    res = Solution().isPalindrome(a)
    print(res)