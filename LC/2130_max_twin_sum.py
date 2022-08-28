from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        res = 0
        n = len(arr)
        for i in range(int(n / 2)):
            res = max(res, arr[i] + arr[n - 1 - i])
        return res