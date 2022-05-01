"""
class ListNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.down=None
"""
import sys
sys.setrecursionlimit(10**9)
# @param root: ListNode
# @return ListNode
def flatten(root):
    if not root or not root.right:
        return root
    mid = get_mid(root)
    h1 = root
    h2 = mid.right
    mid.right = None
    l1 = flatten(root)
    l2 = flatten(h2)
    return merge2Lists(l1, l2)

def get_mid(root):
    if not root or not root.right:
        return root
    slow, fast = root, root
    while fast.right and fast.right.right:
        slow, fast = slow.right, fast.right.right
    return slow

def merge2Lists(h1, h2):
    if not h1 and not h2:
        return h1
    elif not h1:
        return h2
    elif not h2:
        return h1
    if h1.val <= h2.val:
        h1.down = merge2Lists(h1.down, h2)
        return h1
    else:
        h2.down = merge2Lists(h1, h2.down)
        return h2